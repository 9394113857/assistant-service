from datetime import datetime
from app.extensions import db


class AssistantTrainingLog(db.Model):
    __tablename__ = "assistant_training_logs"

    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # User reference
    # NULL allowed for guest users
    user_id = db.Column(db.Integer, nullable=True)

    # Original user message sent to assistant
    user_message = db.Column(db.Text, nullable=False)

    # Intent predicted by ML model or rule-based system
    predicted_intent = db.Column(db.String(100), nullable=False)

    # Confidence score (0–1)
    confidence_score = db.Column(db.Float, nullable=False)

    # Human-corrected intent (used later for retraining)
    actual_intent = db.Column(db.String(100), nullable=True)

    # ML model version used
    model_version = db.Column(db.String(50), nullable=False)

    # Timestamp of interaction
    created_at = db.Column(db.DateTime, default=datetime.utcnow)