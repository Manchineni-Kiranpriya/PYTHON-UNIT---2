def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", a + b)

def factorial():
    n = int(input("Enter a number: "))
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    print("Factorial =", fact)

def even_odd():
    n = int(input("Enter a number: "))

    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def reverse_string():
    text = input("Enter a string: ")
    print("Reversed String:", text[::-1])

while True:
    print("\n----- Utility Services -----")
    print("1. Addition")
    print("2. Factorial")
    print("3. Even/Odd Check")
    print("4. Reverse String")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add()

    elif choice == 2:
        factorial()

    elif choice == 3:
        even_odd()

    elif choice == 4:
        reverse_string()

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
