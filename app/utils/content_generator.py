# utils/content_generator.py
import requests
import json

def generate_content(topic):
    payload = {"topic": topic}
    response = requests.post(CONTENT_GENERATOR_API, json=payload)
    generated_content = response.json()['generated_text']
    return generated_content
