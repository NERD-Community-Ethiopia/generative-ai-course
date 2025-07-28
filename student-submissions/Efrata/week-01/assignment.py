from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "😊 Positive"
    elif polarity < 0:
        return "😞 Negative"
    else:
        return "😐 Neutral"

def main():
    print("📊 Simple Sentiment Analyzer (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        sentiment = analyze_sentiment(user_input)
        print("AI:", sentiment, "\n")

if __name__ == "__main__":
    main()
