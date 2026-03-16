# ==========================================
# Intent Detection Service
# ==========================================

def detect_intent(message: str) -> str:

    msg = message.lower()

    # ----------------------------------
    # Greeting
    # ----------------------------------
    if "hello" in msg or "hi" in msg:
        return "greeting"

    # ----------------------------------
    # Product intents
    # ----------------------------------
    if "show products" in msg or "products" in msg:
        return "show_products"

    if "cheap" in msg or "cheaper" in msg:
        return "cheaper_product"

    if "laptop" in msg or "phone" in msg or "earbuds" in msg:
        return "product_category"

    # ----------------------------------
    # Orders
    # ----------------------------------
    if "order" in msg or "orders" in msg:
        return "show_orders"

    if "track order" in msg:
        return "track_order"

    # ----------------------------------
    # Recommendation
    # ----------------------------------
    if "recommend" in msg:
        return "recommend_product"

    # ----------------------------------
    # Default
    # ----------------------------------
    return "unknown"

