feedback = input("Enter customer feedback: ").lower()

positive_words = [
    "good", "great", "excellent", "amazing", "happy",
    "satisfied", "love", "awesome", "best", "nice"
]

negative_words = [
    "bad", "poor", "terrible", "worst", "hate",
    "disappointed", "not happy", "slow", "problem", "issue", "awful"
]

positive_count = 0
negative_count = 0

for word in positive_words:
    if word in feedback:
        positive_count += 1

for word in negative_words:
    if word in feedback:
        negative_count += 1

if positive_count > negative_count:
    sentiment = "Positive"
elif negative_count > positive_count:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("\nSentiment Category:", sentiment)
