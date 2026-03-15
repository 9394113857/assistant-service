import os
import requests
from flask import request

PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL")
ORDER_SERVICE_URL = os.getenv("ORDER_SERVICE_URL")
CART_SERVICE_URL = os.getenv("CART_SERVICE_URL")
RECO_SERVICE_URL = os.getenv("RECO_SERVICE_URL")


# ==============================
# PRODUCT REQUEST
# ==============================
def handle_product_request():

    try:

        response = requests.get(PRODUCT_SERVICE_URL)

        if response.status_code != 200:
            return "Sorry, product service is temporarily unavailable."

        products = response.json()

        if not products:
            return "No products available."

        result = "Here are some products:\n"

        for p in products[:5]:

            name = p.get("name", "Unknown")
            price = p.get("price", "N/A")

            result += f"- {name} (${price})\n"

        return result

    except Exception:
        return "Product service unavailable."


# ==============================
# ORDER REQUEST
# ==============================
def handle_order_request(user_id: int):

    try:

        token = request.headers.get("Authorization")

        headers = {}

        if token:
            headers["Authorization"] = token

        response = requests.get(
            f"{ORDER_SERVICE_URL}/{user_id}",
            headers=headers
        )

        if response.status_code == 401:
            return "Please login to access your orders."

        if response.status_code != 200:
            return "Could not fetch orders."

        orders = response.json()

        if not orders:
            return "You have no orders."

        result = "Your recent orders:\n"

        for o in orders[:5]:

            order_id = o.get("order_id") or o.get("id")
            status = o.get("status", "unknown")

            result += f"- Order #{order_id} | Status: {status}\n"

        return result

    except Exception:
        return "Order service unavailable."


# ==============================
# RECOMMENDATION REQUEST
# ==============================
def handle_recommendation_request(user_id: int):

    try:

        token = request.headers.get("Authorization")

        headers = {}

        if token:
            headers["Authorization"] = token

        response = requests.get(
            f"{RECO_SERVICE_URL}/{user_id}",
            headers=headers
        )

        if response.status_code != 200:
            return "Recommendation service unavailable."

        recos = response.json()

        if not recos:
            return "No recommendations available yet."

        result = "Recommended for you:\n"

        for r in recos[:5]:

            product_id = r.get("product_id")

            result += f"- Product ID: {product_id}\n"

        return result

    except Exception:
        return "Could not fetch recommendations."