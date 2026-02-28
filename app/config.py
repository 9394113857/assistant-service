import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ✅ If DATABASE_URL exists → use it (production)
    # ✅ Else → use SQLite locally
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///assistant.db"
    )