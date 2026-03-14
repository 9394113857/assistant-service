def resolve_followup(message: str, previous_messages: list) -> str:
    """
    Detect follow-up queries and expand them using conversation context.
    """

    message_lower = message.lower()

    # If message already contains clear keywords → return as is
    if any(word in message_lower for word in [
        "product", "item", "order", "recommend", "cart"
    ]):
        return message

    # Look into previous conversation
    for msg in reversed(previous_messages):

        text = msg.lower()

        if "product" in text or "show products" in text:
            if "recommend" in message_lower or "one" in message_lower:
                return "recommend product"

            if "cheaper" in message_lower:
                return "cheap product"

        if "order" in text:
            if "status" in message_lower:
                return "order status"

    return message