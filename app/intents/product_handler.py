from app.intents.base_handler import BaseIntentHandler
from app.services.tool_router import handle_product_request


class ProductHandler(BaseIntentHandler):

    def handle(self, user_id: int, message: str) -> str:

        try:
            response = handle_product_request(message)

            # If router returned empty
            if not response:
                return (
                    "Sorry, I couldn't find any products matching your request."
                )

            return response

        except Exception:
            return (
                "Sorry, I couldn't reach the product service right now."
            )