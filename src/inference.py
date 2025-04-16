import joblib
import os
import tensorflow as tf
import re
from src.config import max_seq_len, ASSETS_Path, vocab_size

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

class SentimentAnalyzer:
    def __init__(self):
        print("[INFO] Loading model and word2idx...")
        self.model = tf.keras.models.load_model(os.path.join(ASSETS_Path, "model.keras"))
        self.word2idx = joblib.load(os.path.join(ASSETS_Path, "word2idx.joblib"))
        print("[INFO] Model and word2idx loaded successfully.")
        self.unknown_token = 0  # Set an unknown token (0 by default)

    def predict(self, text: str):
        cleaned_text = preprocess_text(text)
        # Ensure that out-of-vocabulary words are replaced with 0
        encoded_text = [self.word2idx.get(word, self.unknown_token) for word in cleaned_text.split()]

        encoded_text = [idx if idx < vocab_size else self.unknown_token for idx in encoded_text]

        preprocessed_text = tf.keras.preprocessing.sequence.pad_sequences(
            [encoded_text], maxlen=max_seq_len, padding='post', truncating='post', value=0
        )
        prob = self.model.predict(preprocessed_text)[0][0]
        sentiment = "Positive" if prob > 0.5 else "Negative"
        confidence = prob if sentiment == "Positive" else 1 - prob
        return sentiment, float(confidence)



