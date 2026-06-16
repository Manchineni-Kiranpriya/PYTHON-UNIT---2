n = int(input("Enter the number of subjects: "))

total = 0

for i in range(n):
    marks = int(input(f"Enter marks for Subject {i+1}: "))
    total += marks

average = total / n

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\nAcademic Performance Summary")
print("----------------------------")
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
