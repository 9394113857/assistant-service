from .ml_model_loader import get_model


def detect_intent(message: str):
    """
    Hybrid Intent Detection:
    - If ML model exists → use ML
    - If not → fallback to rule-based
    """

    model, model_version = get_model()

    message = message.lower()

    # ==========================================================
    # 1️⃣ If ML Model Exists → Use It
    # ==========================================================
    if model:
        prediction = model.predict([message])[0]

        # Try to calculate confidence if classifier supports it
        try:
            confidence = max(model.predict_proba([message])[0])
        except Exception:
            confidence = 0.90  # Default confidence fallback

        return prediction, float(confidence), model_version

    # ==========================================================
    # 2️⃣ Fallback Rule-Based (Safety Layer)
    # ==========================================================
    if any(word in message for word in ["order", "track", "status"]):
        return "order", 1.0, "rule_based_v1"

    if any(word in message for word in ["product", "item", "show"]):
        return "product", 1.0, "rule_based_v1"

    if any(word in message for word in ["cart"]):
        return "cart", 1.0, "rule_based_v1"

    if any(word in message for word in ["recommend", "suggest"]):
        return "recommendation", 1.0, "rule_based_v1"

    return "general", 1.0, "rule_based_v1"