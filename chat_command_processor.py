command = input("Enter a command: ").lower()

if command == "hello":
    print("Hi! How can I help you?")
elif command == "time":
    print("Current time feature is selected.")
elif command == "help":
    print("Available commands: hello, time, help, exit")
elif command == "exit":
    print("Exiting chat...")
else:
    print("Unknown command")
