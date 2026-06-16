score = 0

print("Quiz")
print("-----------")

answer = input("1. What is the capital of India? ")
if answer.lower() == "new delhi":
    score += 1

answer = input("2. How many days are there in a week? ")
if answer == "7":
    score += 1

answer = input("3. What is 5 + 3? ")
if answer == "8":
    score += 1

print("\nQuiz Completed!")
print("Your Score:", score, "/ 3")
