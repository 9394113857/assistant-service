def detect_intent(message: str) -> str:
    """
    Very basic intent detection using keyword matching.
    Free and simple.
    """

    message = message.lower()

    if any(word in message for word in ["order", "track", "status"]):
        return "order"

    if any(word in message for word in ["product", "item", "show"]):
        return "product"

    if any(word in message for word in ["cart"]):
        return "cart"

    if any(word in message for word in ["recommend", "suggest"]):
        return "recommendation"

    return "general"