total_reviews = int(input("Enter number of reviews: "))

total_rating = 0

for i in range(total_reviews):
    rating = float(input(f"Enter rating {i+1} (1-5): "))
    total_rating += rating

average = total_rating / total_reviews

print("\nAverage Rating:", round(average, 2))

if average >= 4.5:
    print("Performance Summary: Excellent")
elif average >= 3.5:
    print("Performance Summary: Good")
elif average >= 2.5:
    print("Performance Summary: Average")
else:
    print("Performance Summary: Poor")
