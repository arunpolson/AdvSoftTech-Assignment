from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

def load_model(model_path=None):
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    labels = ["Negative", "Positive"]
    return tokenizer, model, labels
