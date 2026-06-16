first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = input("Enter your birth year: ")

username1 = first_name.lower() + last_name.lower()
username2 = first_name.lower() + birth_year
username3 = first_name[0].lower() + last_name.lower() + birth_year[-2:]

print("\nSuggested Usernames:")
print(username1)
print(username2)
print(username3)
