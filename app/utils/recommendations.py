# utils/recommendations.py
from keras.models import load_model
from config import MODEL_PATH

model = load_model(MODEL_PATH)

def predict_rating(user_id, post_id):
    prediction = model.predict([[user_id], [post_id]])[0][0]
    return float(prediction)
