from flask import Blueprint, request, jsonify
from models import OutreachSequence, db

sequence_bp = Blueprint("sequence", __name__)

@sequence_bp.route("/", methods=["POST"])
def generate_sequence():
    data = request.json
    user_id = data.get("user_id")
    sequence_text = data.get("sequence_text", "")

    if not user_id or not sequence_text:
        return jsonify({"error": "Missing data"}), 400

    sequence = OutreachSequence(user_id=user_id, sequence_text=sequence_text)
    db.session.add(sequence)
    db.session.commit()

    return jsonify({"message": "Sequence saved successfully", "sequence_id": sequence.id})
