msg = input("Enter encrypted text: ")

result = ""

for ch in msg:
    result += chr(ord(ch) - 2)

print("Decrypted Text:", result)
