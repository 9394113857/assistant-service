from app.intents.base_handler import BaseIntentHandler
from app.services.tool_router import handle_product_request


class ProductHandler(BaseIntentHandler):

    def handle(self, user_id: int, message: str) -> str:

        try:
            products = handle_product_request(message)

            # If API returned nothing
            if not products:
                return (
                    "Sorry, I couldn't find any products matching your request. "
                    "You can try asking for phones, laptops, earbuds, or watches."
                )

            # If API already formatted response
            if isinstance(products, str):
                return products

            # Format product list safely
            response = "Here are some products:\n"

            for p in products[:5]:
                name = p.get("name", "Unknown Product")
                price = p.get("price", "N/A")

                response += f"- {name} (${price})\n"

            return response.strip()

        except Exception:
            return "Sorry, product service is temporarily unavailable. Please try again later."