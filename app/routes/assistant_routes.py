from flask import Blueprint, request, jsonify
from app.services.assistant_orchestrator import process_user_message

assistant_bp = Blueprint("assistant", __name__)

@assistant_bp.post("/chat")
def chat():

    data = request.json or {}

    user_id = data.get("user_id")   # optional now
    message = data.get("message")

    if not message:
        return jsonify({"error": "message is required"}), 400

    result = process_user_message(user_id, message)

    return jsonify(result)