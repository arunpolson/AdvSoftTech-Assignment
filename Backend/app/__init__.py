from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def load_model():
    analyzer = SentimentIntensityAnalyzer()
    labels = ["Negative", "Neutral", "Positive"]
    return analyzer, labels

# Makes 'app' a Python package (can be left empty)# Makes 'app' a Python package (can be left empty)
