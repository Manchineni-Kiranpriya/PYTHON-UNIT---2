string = input("Enter a string: ")
for ch in string:
    count = 0
    for c in string:
        if ch == c:
            count = count + 1
    print(ch, ":", count)
