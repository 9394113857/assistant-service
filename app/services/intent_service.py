# ==========================================
# Intent Detection Service
# ==========================================

def detect_intent(message: str):
    """
    Returns:
        intent
        confidence_score
        model_version
    """

    msg = message.lower()

    intent = "unknown"
    confidence = 0.75
    model_version = "rule_v1"

    # ----------------------------------
    # Greeting
    # ----------------------------------
    if "hello" in msg or "hi" in msg:
        intent = "greeting"
        confidence = 0.95

    # ----------------------------------
    # Product intents
    # ----------------------------------
    elif "product" in msg or "products" in msg:
        intent = "show_products"
        confidence = 0.90

    elif "cheap" in msg or "cheaper" in msg:
        intent = "cheaper_product"
        confidence = 0.85

    elif "phone" in msg or "laptop" in msg or "earbuds" in msg:
        intent = "product_category"
        confidence = 0.80

    # ----------------------------------
    # Orders
    # ----------------------------------
    elif "order" in msg or "orders" in msg:
        intent = "show_orders"
        confidence = 0.90

    elif "track" in msg:
        intent = "track_order"
        confidence = 0.85

    # ----------------------------------
    # Recommendation
    # ----------------------------------
    elif "recommend" in msg:
        intent = "recommend_product"
        confidence = 0.85

    return intent, confidence, model_version