from transformers import AutoTokenizer, AutoModelForSequenceClassification

def load_model(model_path=None):
    model_name = "mrm8488/bert-tiny-finetuned-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    labels = ["Negative", "Positive"]  # Adjust if needed
    return tokenizer, model, labels
