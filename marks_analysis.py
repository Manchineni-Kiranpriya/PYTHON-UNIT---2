n = int(input("Enter number of subjects: "))

total = 0

for i in range(n):
    marks = int(input("Enter marks for Subject " + str(i + 1) + ": "))
    total += marks

average = total / n
percentage = average

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- Performance Report -----")
print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage, "%")
print("Grade:", grade)
