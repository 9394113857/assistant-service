from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.chat_session import ChatSession
from app.models.chat_message import ChatMessage

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

    # 🔁 Create new session (basic)
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

    # 🧠 Detect intent
    intent = detect_intent(message)

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
    db.session.commit()

    return jsonify({"response": assistant_reply})