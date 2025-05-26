# 1. app.py - expose le modèle via Flask
from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
model = joblib.load("RandomForest.pkl")
features = model.feature_names_in_

@app.route("/", methods=["GET"])
def health_check():
    return "OK", 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        inputs = pd.DataFrame([data], columns=features)
        prediction = model.predict(inputs)[0]
        proba = model.predict_proba(inputs)[0].tolist()
        return jsonify({"prediction": int(prediction), "probability": proba})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
