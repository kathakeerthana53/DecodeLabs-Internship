from textblob import TextBlob

text = input("Enter a sentence: ")

analysis = TextBlob(text)

polarity = analysis.sentiment.polarity

if polarity > 0:
    sentiment = "POSITIVE"
elif polarity < 0:
    sentiment = "NEGATIVE"
else:
    sentiment = "NEUTRAL"

print("\nRecognition Result:")
print("-------------------")
print("Text:", text)
print("Sentiment:", sentiment)
print("Polarity Score:", polarity)