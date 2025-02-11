from flask import Blueprint, request, jsonify
from services.ai_service import process_chat

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = process_chat(user_input)
    return jsonify({"response": response})
