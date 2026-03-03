from flask import Blueprint, request, jsonify
from app.services.assistant_orchestrator import process_user_message

assistant_bp = Blueprint("assistant", __name__)

@assistant_bp.post("/chat")
def chat():

    data = request.json
    user_id = data.get("user_id")
    message = data.get("message")

    if not user_id or not message:
        return jsonify({"error": "user_id and message are required"}), 400

    result = process_user_message(user_id, message)

    return jsonify(result)