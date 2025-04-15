from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Make sure the lexicon is downloaded
nltk.download('vader_lexicon', quiet=True)

# Initialize VADER analyzer
sia = SentimentIntensityAnalyzer()

def detect_sentiment(text):
    # Custom keyword overrides for better emotion detection
    lowered = text.lower()

    if any(word in lowered for word in ["anxious", "depressed", "worthless", "hopeless", "panic", "hate myself", "sad", "lonely", "i feel terrible", "i don’t feel good"]):
        return "negative"
    if any(word in lowered for word in ["happy", "grateful", "excited", "hopeful", "relieved", "calm", "peaceful", "joy"]):
        return "positive"

    # Fallback to VADER analysis
    score = sia.polarity_scores(text)
    compound = score['compound']

    if compound >= 0.05:
        return "positive"
    elif compound <= -0.05:
        return "negative"
    else:
        return "neutral"
