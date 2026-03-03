from app.intents.base_handler import BaseIntentHandler


class UnknownHandler(BaseIntentHandler):

    def handle(self, user_id: int, message: str) -> str:
        return (
            "I'm not fully sure what you mean. "
            "I can help with products, orders, or recommendations."
        )