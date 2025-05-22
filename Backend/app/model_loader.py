from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

def load_model(model_path=None):
    if model_path is None:
        model_path = os.path.join(os.path.dirname(__file__), "sentiment_model")
    if not os.path.exists(model_path):
        # Download from HuggingFace if not present
        model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        os.makedirs(model_path, exist_ok=True)
        tokenizer.save_pretrained(model_path)
        model.save_pretrained(model_path)
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSequenceClassification.from_pretrained(model_path)
    labels = ["Negative", "Slightly Negative", "neutral", "Positive", "Slightly Positive"]
    return tokenizer, model, labels
