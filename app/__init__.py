import os
import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask, jsonify, request
from .config import Config
from .extensions import db, migrate
from flask_cors import CORS


def create_app(testing: bool = False):
    app = Flask(__name__)

    # --------------------------
    # Base Config
    # --------------------------
    app.config.from_object(Config)

    if testing:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["SECRET_KEY"] = "test-secret"

    # --------------------------
    # Extensions
    # --------------------------
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # --------------------------
    # Logging Setup
    # --------------------------
    logs_path = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_path, exist_ok=True)

    log_file = os.path.join(logs_path, "assistant.log")

    handler = TimedRotatingFileHandler(
        log_file,
        when="midnight",
        interval=1,
        backupCount=30,
        encoding="utf-8"
    )

    handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    ))

    if not app.logger.handlers:
        app.logger.addHandler(handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info("Assistant service starting...")

    # --------------------------
    # Log Every Request
    # --------------------------
    @app.before_request
    def log_request():
        app.logger.info(
            f"Incoming {request.method} {request.path}"
        )

    @app.after_request
    def log_response(response):
        app.logger.info(
            f"Response {response.status}"
        )
        return response

    # --------------------------
    # Register Routes
    # --------------------------
    from .routes.assistant_routes import assistant_bp
    app.register_blueprint(assistant_bp, url_prefix="/api/v1/assistant")

    # --------------------------
    # Health Check (Render/Railway)
    # --------------------------
    @app.get("/")
    def health():
        return jsonify({
            "status": "Assistant service running successfully."
        }), 200

    app.logger.info("Assistant service started successfully.")
    return app