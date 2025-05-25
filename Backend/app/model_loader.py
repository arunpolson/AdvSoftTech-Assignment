from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def load_model():
    analyzer = SentimentIntensityAnalyzer()
    labels = ["Negative", "Neutral", "Positive"]
    return analyzer, labels

# In your predictor:
def predict_sentiment(text, analyzer, labels):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        label = "Positive"
    elif compound <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"
    return {"label": label, "scores": scores}

result = predict_sentiment(str(text), analyzer, labels)
row = {
    "text": text,
    "label": result["label"],
    "negative": result["scores"]["neg"],
    "neutral": result["scores"]["neu"],
    "positive": result["scores"]["pos"],
    "compound": result["scores"]["compound"]
}
rows.append(row)
