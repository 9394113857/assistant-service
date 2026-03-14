def resolve_followup(message: str, previous_messages: list) -> str:
    """
    Resolve follow-up conversational queries
    using recent conversation context.
    """

    message_lower = message.lower()

    # If message already contains product/order keywords
    if any(word in message_lower for word in [
        "product", "products", "item", "items",
        "order", "orders", "recommend"
    ]):
        return message

    # Check previous context
    for msg in reversed(previous_messages):

        text = msg.lower()

        if "product" in text or "show products" in text:

            if "recommend" in message_lower or "one" in message_lower:
                return "recommend product"

            if "cheap" in message_lower or "cheaper" in message_lower:
                return "cheap product"

            if "laptop" in message_lower:
                return "show laptop products"

            if "phone" in message_lower:
                return "show phone products"

    return message