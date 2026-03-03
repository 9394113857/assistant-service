from app.extensions import db
from app.models.chat_session import ChatSession
from app.models.chat_message import ChatMessage
from app.models.assistant_training_log import AssistantTrainingLog

from app.services.intent_service import detect_intent
from app.services.intent_registry import get_intent_handler

CONFIDENCE_THRESHOLD = 0.60


def process_user_message(user_id, message):

    # Create session
    session = ChatSession(user_id=user_id)
    db.session.add(session)
    db.session.commit()

    # Save user message
    db.session.add(ChatMessage(
        session_id=session.id,
        role="user",
        message=message
    ))
    db.session.commit()

    # Detect intent
    intent, confidence_score, model_version = detect_intent(message)

    if confidence_score is not None and confidence_score < CONFIDENCE_THRESHOLD:
        intent = "unknown"

    # Load handler dynamically
    handler = get_intent_handler(intent)
    assistant_reply = handler.handle(user_id=user_id, message=message)

    # Save assistant reply
    db.session.add(ChatMessage(
        session_id=session.id,
        role="assistant",
        message=assistant_reply
    ))

    # Save training log
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