correct_answers = ["A", "B", "C", "D", "A"]

score = 0

for i in range(5):
    answer = input(f"Enter answer for Question {i+1}: ").upper()

    if answer == correct_answers[i]:
        score += 1

percentage = (score / 5) * 100

print("\nTotal Score:", score)
print("Percentage:", percentage, "%")

if percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
