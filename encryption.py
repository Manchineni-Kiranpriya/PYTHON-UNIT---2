message = input("Enter a message: ")

encrypted = ""

for ch in message:
    encrypted += chr(ord(ch) + 2)

print("Encrypted Message:", encrypted)
