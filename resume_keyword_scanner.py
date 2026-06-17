resume = input("Paste the resume text:\n").lower()

keywords = [
    "python", "java", "sql", "html", "css",
    "javascript", "machine learning", "data analysis",
    "communication", "leadership"
]

found_keywords = []

for keyword in keywords:
    if keyword in resume:
        found_keywords.append(keyword)

print("\nKeywords Found:")

if found_keywords:
    for word in found_keywords:
        print("-", word)
else:
    print("No matching keywords found.")
