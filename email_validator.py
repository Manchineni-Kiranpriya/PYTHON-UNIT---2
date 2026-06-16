email = input("Enter an email address: ")

if "@" in email and email.count("@") == 1:
    username, domain = email.split("@")

    if username != "" and "." in domain and not domain.startswith(".") and not domain.endswith("."):
        print("Valid email address")
    else:
        print("Invalid email address")
else:
    print("Invalid email address")
