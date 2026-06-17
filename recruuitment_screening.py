age = int(input("Enter Age: "))
qualification = input("Enter Qualification (UG/PG): ").upper()
percentage = float(input("Enter Percentage: "))

if age >= 18 and qualification in ["UG", "PG"] and percentage >= 60:
    print("\nCandidate is Eligible for Recruitment.")
else:
    print("\nCandidate is Not Eligible for Recruitment.")
    
