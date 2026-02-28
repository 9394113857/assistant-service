import os
import requests

# 🔁 Replace these with your real service URLs
# PRODUCT_SERVICE_URL = "http://localhost:5002/api/products"
# ORDER_SERVICE_URL = "http://localhost:5003/api/orders"
# RECO_SERVICE_URL = "http://localhost:5005/api/recommendations"

# 🔁 Replace these with your real service URLs from Railway now:-
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL")
ORDER_SERVICE_URL = os.getenv("ORDER_SERVICE_URL")
CART_SERVICE_URL = os.getenv("CART_SERVICE_URL")
RECO_SERVICE_URL = os.getenv("RECO_SERVICE_URL")


def handle_product_request():
    try:
        response = requests.get(PRODUCT_SERVICE_URL)
        if response.status_code == 200:
            products = response.json()

            if not products:
                return "No products available."

            result = "Here are some products:\n"
            for p in products[:5]:
                result += f"- {p.get('name')} (${p.get('price')})\n"

            return result

        return "Could not fetch products."

    except Exception:
        return "Product service unavailable."


def handle_order_request(user_id: int):
    try:
        response = requests.get(f"{ORDER_SERVICE_URL}/{user_id}")

        if response.status_code == 200:
            orders = response.json()

            if not orders:
                return "You have no orders."

            result = "Your recent orders:\n"
            for o in orders[:5]:
                result += f"- Order #{o.get('id')} | Status: {o.get('status')}\n"

            return result

        return "Could not fetch orders."

    except Exception:
        return "Order service unavailable."


def handle_recommendation_request(user_id: int):
    try:
        response = requests.get(f"{RECO_SERVICE_URL}/{user_id}")

        if response.status_code == 200:
            recos = response.json()

            if not recos:
                return "No recommendations available."

            result = "Recommended for you:\n"
            for r in recos[:5]:
                result += f"- Product ID: {r.get('product_id')}\n"

            return result

        return "Could not fetch recommendations."

    except Exception:
        return "Recommendation service unavailable."