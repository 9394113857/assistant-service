import os
import joblib

MODEL_PATH = os.path.join(
    os.getcwd(),
    "models",
    "assistant_intent_model.pkl"
)

model = None
model_version = "ml_v1"

def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print("✅ ML model loaded successfully.")
    else:
        print("⚠ ML model not found. Falling back to rule-based.")

def get_model():
    return model, model_version