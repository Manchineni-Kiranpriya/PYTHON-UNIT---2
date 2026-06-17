message = input("Enter a message: ").lower()

spam_keywords = [
    "win", "prize", "free", "offer",
    "lottery", "money", "click",
    "urgent", "congratulations"
]

spam_count = 0

for word in spam_keywords:
    if word in message:
        spam_count += 1

if spam_count > 0:
    print("\nSpam Message Detected!")
else:
    print("\nNot a Spam Message.")
