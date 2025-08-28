# utils/ml.py
import requests
import json

def generate_recommendation(user_id, content):
    payload = {"user_id": user_id, "content": content}
    response = requests.post(ML_MODEL_ENDPOINT, json=payload)
    recommended_item = response.json()['recommended_item']
    return recommended_item
