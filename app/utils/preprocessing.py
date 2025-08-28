# utils/preprocessing.py
import re

def clean_text(text):
    cleaned = re.sub(r'\W+', ' ', text.lower()).strip()
    return cleaned
