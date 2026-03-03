from app.intents.base_handler import BaseIntentHandler
from app.services.tool_router import handle_order_request


class OrderHandler(BaseIntentHandler):

    def handle(self, user_id: int, message: str) -> str:
        return handle_order_request(user_id)