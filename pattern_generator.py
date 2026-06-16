choice = int(input("Select a pattern:\n"
                   "1. Star Triangle\n"
                   "2. Number Triangle\n"
                   "3. Alphabet Triangle\n"
                   "Enter your choice: "))

if choice == 1:
    n = int(input("Enter number of rows: "))
    print("\nStar Triangle")
    for i in range(1, n + 1):
        print("*" * i)

elif choice == 2:
    n = int(input("Enter number of rows: "))
    print("\nNumber Triangle")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

elif choice == 3:
    n = int(input("Enter number of rows: "))
    print("\nAlphabet Triangle")
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()

else:
    print("Invalid Choice")
