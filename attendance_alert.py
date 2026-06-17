n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    total = int(input("Enter total classes: "))
    attended = int(input("Enter attended classes: "))

    percentage = (attended / total) * 100

    print("Attendance Percentage:", round(percentage, 2), "%")

    if percentage < 75:
        print("Alert:", name, "has low attendance!")
    else:
        print(name, "has satisfactory attendance.")
