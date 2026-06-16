text = input("Enter a text: ")

# Remove extra spaces
formatted_text = " ".join(text.split())

print("\nOriginal Text:", text)
print("Without Extra Spaces:", formatted_text)

# Case Conversion
print("Uppercase:", formatted_text.upper())
print("Lowercase:", formatted_text.lower())

# Alignment
print("\nLeft Aligned:")
print(formatted_text.ljust(30))

print("\nCenter Aligned:")
print(formatted_text.center(30))

print("\nRight Aligned:")
print(formatted_text.rjust(30))
