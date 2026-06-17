qualification = input("Enter Qualification: ")
percentage = float(input("Enter Percentage: "))
skill = input("Enter Skill: ")

if (qualification.lower() in ["degree", "btech", "mtech", "mca"] and
    percentage >= 60 and
    skill.lower() == "python"):
    
    print("Candidate is Eligible")
else:
    print("Candidate is Not Eligible")
