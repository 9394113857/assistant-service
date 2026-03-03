from .ml_model_loader import get_model


def detect_intent(message: str):
    """
    Hybrid Intent Detection (Industry Pattern)

    Priority Order:
    1️⃣ Rule-based for simple conversational intents (greeting, thanks)
    2️⃣ ML model for business intents
    3️⃣ Rule-based fallback (safety net)
    """

    message = message.lower().strip()

    # ==========================================================
    # 1️⃣ Rule-Based Conversational Intents (ALWAYS FIRST)
    # ==========================================================

    # Greeting
    if any(word in message for word in [
        "hi", "hello", "hey", "hii", "heyy",
        "good morning", "good evening", "good night"
    ]):
        return "greeting", 1.0, "rule_based_v2"

    # Thanks
    if any(word in message for word in [
        "thank you", "thanks", "thx"
    ]):
        return "greeting", 1.0, "rule_based_v2"

    # Asking assistant name
    if "your name" in message:
        return "greeting", 1.0, "rule_based_v2"

    # How are you
    if "how are you" in message:
        return "greeting", 1.0, "rule_based_v2"

    # ==========================================================
    # 2️⃣ ML Model (Business Intent Detection)
    # ==========================================================

    model, model_version = get_model()

    if model:
        prediction = model.predict([message])[0]

        try:
            confidence = max(model.predict_proba([message])[0])
        except Exception:
            confidence = 0.90

        return prediction, float(confidence), model_version

    # ==========================================================
    # 3️⃣ Rule-Based Business Fallback (Safety Layer)
    # ==========================================================

    if any(word in message for word in ["order", "track", "status"]):
        return "order", 1.0, "rule_based_v1"

    if any(word in message for word in ["product", "item", "show", "display"]):
        return "product", 1.0, "rule_based_v1"

    if "cart" in message:
        return "cart", 1.0, "rule_based_v1"

    if any(word in message for word in ["recommend", "suggest"]):
        return "recommendation", 1.0, "rule_based_v1"

    # ==========================================================
    # 4️⃣ Final Safe Fallback
    # ==========================================================

    return "general", 0.5, "rule_based_v1"