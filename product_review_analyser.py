positive_words = ["good", "great", "excellent", "amazing", "best", "love"]
negative_words = ["bad", "poor", "worst", "terrible", "hate", "awful"]

n = int(input("Enter number of reviews: "))

positive = 0
negative = 0
neutral = 0

for i in range(n):
    review = input(f"Enter review {i+1}: ").lower()

    pos_count = 0
    neg_count = 0

    for word in positive_words:
        if word in review:
            pos_count += 1

    for word in negative_words:
        if word in review:
            neg_count += 1

    if pos_count > neg_count:
        positive += 1
    elif neg_count > pos_count:
        negative += 1
    else:
        neutral += 1

print("\n----- Review Summary -----")
print("Total Reviews :", n)
print("Positive Reviews :", positive)
print("Negative Reviews :", negative)
print("Neutral Reviews :", neutral)
