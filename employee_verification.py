name = input("Enter Employee Name: ")
age = int(input("Enter Age: "))
qualification = input("Enter Qualification: ")
experience = int(input("Enter Years of Experience: "))

if (name != "" and
    age >= 18 and
    qualification.lower() in ["degree", "btech", "mtech", "mba"] and
    experience >= 1):
    
    print("\nEmployee Details Valid")
    print("Employment Status: Eligible")
else:
    print("\nEmployee Details Invalid")
    print("Employment Status: Not Eligible")
