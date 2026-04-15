from fastapi import FastAPI
import torch
import tensorflow as tf
import numpy as np

from model.feature_extractor import extract_features
from llm.analysis import analyze_code_llama

from model.pytorch_model import CodeQualityModel

# =================================
# SELECT MODEL TYPE HERE
# =================================

MODEL_TYPE = "tensorflow"
# options:
# "pytorch"
# "tensorflow"


app = FastAPI()
label_map = ["bad", "average", "good"]

# =================================
# LOAD MODEL
# =================================

if MODEL_TYPE == "pytorch":
    model = CodeQualityModel()
    model.load_state_dict(
        torch.load("trained_models/pytorch_model.pt")
    )
    model.eval()

elif MODEL_TYPE == "tensorflow":
    model = tf.keras.models.load_model(
        "trained_models/tensorflow_model.keras"
    )

# =================================
# API ENDPOINT
# =================================

@app.post("/analyze")
def analyze(payload: dict):
    code = payload["code"]
    features = extract_features(code)

    if MODEL_TYPE == "pytorch":
        x = torch.tensor(features).float()
        pred = model(x)
        label = label_map[pred.argmax().item()]

    elif MODEL_TYPE == "tensorflow":
        pred = model.predict(np.array([features]))
        label = label_map[pred.argmax()]

    explanation = analyze_code_llama(code)
    return {
        "quality": label,
        "analysis": explanation
    }