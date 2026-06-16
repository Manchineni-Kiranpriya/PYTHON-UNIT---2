password = input("Enter a password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Password is valid.")
    else:
        print("Password is invalid.")
        print("Password must contain:")
        if not has_upper:
            print("- At least one uppercase letter")
        if not has_lower:
            print("- At least one lowercase letter")
        if not has_digit:
            print("- At least one digit")
        if not has_special:
            print("- At least one special character")
else:
    print("Password is invalid.")
    print("Password must be at least 8 characters long.")
