s1 = int(input("Enter marks of Student 1: "))
s2 = int(input("Enter marks of Student 2: "))
s3 = int(input("Enter marks of Student 3: "))

marks = [s1, s2, s3]
marks.sort(reverse=True)

for i in range(len(marks)):
    print("Rank", i + 1, ":", marks[i])
