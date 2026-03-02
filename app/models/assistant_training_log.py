from datetime import datetime
from app.extensions import db


class AssistantTrainingLog(db.Model):
    __tablename__ = "assistant_training_logs"

    id = db.Column(db.Integer, primary_key=True)

    # User reference
    user_id = db.Column(db.Integer, nullable=False)

    # Original user message
    user_message = db.Column(db.Text, nullable=False)

    # System prediction
    predicted_intent = db.Column(db.String(100), nullable=False)

    # Confidence score (0–1)
    confidence_score = db.Column(db.Float, nullable=False)

    # Human-corrected intent (for retraining)
    actual_intent = db.Column(db.String(100), nullable=True)

    # Model version used for prediction
    model_version = db.Column(db.String(50), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)