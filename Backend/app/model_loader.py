from transformers import AutoTokenizer, AutoModelForSequenceClassification

def load_model(model_path="./sentiment_model"):
    tokenizer = AutoTokenizer.from_pretrained('Backend/app/sentiment_model')
model = AutoModelForSequenceClassification.from_pretrained('Backend/app/sentiment_model')
 labels = ["Negative", "Slightly Negative", "neutral", "Positive", "Slightly Positive"]
    return tokenizer, model, labels
