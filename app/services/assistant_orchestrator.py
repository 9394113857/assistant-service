from app.extensions import db
from app.models.chat_session import ChatSession
from app.models.chat_message import ChatMessage
from app.models.assistant_training_log import AssistantTrainingLog

from app.services.intent_service import detect_intent
from app.services.intent_registry import get_intent_handler

# Minimum ML confidence required
CONFIDENCE_THRESHOLD = 0.60

# Intents that require a logged-in user
LOGIN_REQUIRED_INTENTS = {"order", "recommendation"}

# Keywords that also indicate login-required actions
LOGIN_REQUIRED_KEYWORDS = ["order", "track", "status", "recommend"]


def process_user_message(user_id, message):

    message_lower = message.lower()

    # ---------------------------------------------------
    # SESSION MANAGEMENT
    # Reuse latest session
    # ---------------------------------------------------
    session = (
        ChatSession.query
        .filter_by(user_id=user_id)
        .order_by(ChatSession.created_at.desc())
        .first()
    )

    if not session:
        session = ChatSession(user_id=user_id)
        db.session.add(session)
        db.session.commit()

    # ---------------------------------------------------
    # FEATURE 2: Load conversation context
    # (for future follow-up intelligence)
    # ---------------------------------------------------
    recent_messages = (
        ChatMessage.query
        .filter_by(session_id=session.id)
        .order_by(ChatMessage.id.desc())
        .limit(3)
        .all()
    )

    conversation_context = [
        f"{msg.role}: {msg.message}"
        for msg in reversed(recent_messages)
    ]

    # ---------------------------------------------------
    # Save user message
    # ---------------------------------------------------
    db.session.add(ChatMessage(
        session_id=session.id,
        role="user",
        message=message
    ))
    db.session.commit()

    # ---------------------------------------------------
    # Intent Detection (FIXED)
    # Only use current message for ML
    # ---------------------------------------------------
    intent, confidence_score, model_version = detect_intent(message)

    if confidence_score is not None and confidence_score < CONFIDENCE_THRESHOLD:
        intent = "unknown"

    if intent == "general":
        intent = "unknown"

    # ---------------------------------------------------
    # Login restriction
    # ---------------------------------------------------
    if user_id is None and (
        intent in LOGIN_REQUIRED_INTENTS
        or any(k in message_lower for k in LOGIN_REQUIRED_KEYWORDS)
    ):

        assistant_reply = (
            "Please login to access orders and personalized recommendations."
        )

        db.session.add(ChatMessage(
            session_id=session.id,
            role="assistant",
            message=assistant_reply
        ))

        db.session.add(AssistantTrainingLog(
            user_id=user_id,
            user_message=message,
            predicted_intent=intent,
            confidence_score=confidence_score,
            model_version=model_version
        ))

        db.session.commit()

        return {
            "response": assistant_reply,
            "intent": intent,
            "confidence": confidence_score,
            "model_version": model_version
        }

    # ---------------------------------------------------
    # Load handler
    # ---------------------------------------------------
    handler = get_intent_handler(intent)

    assistant_reply = handler.handle(user_id=user_id, message=message)

    # ---------------------------------------------------
    # Save assistant reply
    # ---------------------------------------------------
    db.session.add(ChatMessage(
        session_id=session.id,
        role="assistant",
        message=assistant_reply
    ))

    # ---------------------------------------------------
    # Save training log
    # ---------------------------------------------------
    db.session.add(AssistantTrainingLog(
        user_id=user_id,
        user_message=message,
        predicted_intent=intent,
        confidence_score=confidence_score,
        model_version=model_version
    ))

    db.session.commit()

    return {
        "response": assistant_reply,
        "intent": intent,
        "confidence": confidence_score,
        "model_version": model_version
    }