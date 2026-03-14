from .ml_model_loader import get_model


def detect_intent(message: str):

    message = message.lower().strip()

    # Rule-based conversational intents
    if any(word in message for word in [
        "hi", "hello", "hey", "hii", "heyy",
        "good morning", "good evening", "good night"
    ]):
        return "greeting", 1.0, "rule_based_v2"

    if any(word in message for word in [
        "thank you", "thanks", "thx"
    ]):
        return "greeting", 1.0, "rule_based_v2"

    if "your name" in message:
        return "greeting", 1.0, "rule_based_v2"

    if "how are you" in message:
        return "greeting", 1.0, "rule_based_v2"

    # ML Model
    model, model_version = get_model()

    if model:
        prediction = model.predict([message])[0]

        try:
            confidence = max(model.predict_proba([message])[0])
        except Exception:
            confidence = 0.90

        return prediction, float(confidence), model_version

    # Rule fallback
    if any(word in message for word in ["order", "track", "status"]):
        return "order", 1.0, "rule_based_v1"

    if any(word in message for word in ["product", "item", "show", "display"]):
        return "product", 1.0, "rule_based_v1"

    if any(word in message for word in ["recommend", "suggest"]):
        return "recommendation", 1.0, "rule_based_v1"

    return "unknown", 0.5, "rule_based_v1"