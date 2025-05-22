from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

def load_model(model_path=None):
    if model_path is None:
        # Always resolve path relative to this file
        model_path = os.path.join(os.path.dirname(__file__), "sentiment_model")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    labels = ["Negative", "Slightly Negative", "neutral", "Positive", "Slightly Positive"]
    return tokenizer, model, labels
