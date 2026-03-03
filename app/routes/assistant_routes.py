from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.chat_session import ChatSession
from app.models.chat_message import ChatMessage
from app.models.assistant_training_log import AssistantTrainingLog

from app.services.intent_service import detect_intent
from app.services.tool_router import (
    handle_product_request,
    handle_order_request,
    handle_recommendation_request
)

assistant_bp = Blueprint("assistant", __name__)


@assistant_bp.post("/chat")
def chat():

    data = request.json
    user_id = data.get("user_id")
    message = data.get("message")

    if not user_id or not message:
        return jsonify({"error": "user_id and message are required"}), 400

    # 🔁 Create new session
    session = ChatSession(user_id=user_id)
    db.session.add(session)
    db.session.commit()

    # Save user message
    user_msg = ChatMessage(
        session_id=session.id,
        role="user",
        message=message
    )
    db.session.add(user_msg)
    db.session.commit()

    # 🧠 Detect intent (ML + Fallback Hybrid)
    intent, confidence_score, model_version = detect_intent(message)

    # 🎛 Route based on intent
    if intent == "product":
        assistant_reply = handle_product_request()

    elif intent == "order":
        assistant_reply = handle_order_request(user_id)

    elif intent == "recommendation":
        assistant_reply = handle_recommendation_request(user_id)

    else:
        assistant_reply = (
            "I can help with products, orders, or recommendations."
        )

    # Save assistant reply
    assistant_msg = ChatMessage(
        session_id=session.id,
        role="assistant",
        message=assistant_reply
    )
    db.session.add(assistant_msg)

    # 🔥 Save training log entry (Very Important for ML Retraining)
    training_log = AssistantTrainingLog(
        user_id=user_id,
        user_message=message,
        predicted_intent=intent,
        confidence_score=confidence_score,
        model_version=model_version
    )
    db.session.add(training_log)

    # Commit everything together
    db.session.commit()

    return jsonify({
        "response": assistant_reply,
        "intent": intent,
        "confidence": confidence_score,
        "model_version": model_version
    })


# So your system now:

# ✔ Uses ML if available
# ✔ Falls back safely if not
# ✔ Logs model version
# ✔ Logs confidence score
# ✔ Returns intent metadata