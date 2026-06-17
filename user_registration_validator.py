username = input("Enter Username: ")
password = input("Enter Password: ")
email = input("Enter Email: ")
age = int(input("Enter Age: "))

if (len(username) >= 5 and
    len(password) >= 8 and
    "@" in email and
    email.count("@") == 1 and
    "." in email.split("@")[1] and
    age >= 18):

    print("\nRegistration Successful")
else:
    print("\nRegistration Failed")
