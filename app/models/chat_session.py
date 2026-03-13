from datetime import datetime
from app.extensions import db


class ChatSession(db.Model):
    __tablename__ = "chat_sessions"

    # Primary key for each chat session
    id = db.Column(db.Integer, primary_key=True)

    # User ID can be NULL for guest users
    # Logged-in users will have a real user_id
    user_id = db.Column(db.Integer, nullable=True)

    # Timestamp when session was created
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship with chat messages
    messages = db.relationship(
        "ChatMessage",
        backref="session",
        lazy=True
    )

# flask db migrate -m "allow guest chat sessions"    
# flask db upgrade