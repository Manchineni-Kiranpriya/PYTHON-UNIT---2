balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited:", amount)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Amount Withdrawn:", amount)
    else:
        print("Insufficient Balance")

def check_balance():
    print("Current Balance:", balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance Enquiry")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice == 3:
        check_balance()

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
