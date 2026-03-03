from app.intents.base_handler import BaseIntentHandler
from app.services.tool_router import handle_product_request


class ProductHandler(BaseIntentHandler):

    def handle(self, user_id: int, message: str) -> str:
        return handle_product_request()