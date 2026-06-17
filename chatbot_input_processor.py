query = input("Enter your query: ").lower()

if "hello" in query:
    print("Response: Hello! How can I help you?")
elif "price" in query:
    print("Response: Please visit our website for pricing details.")
elif "contact" in query:
    print("Response: You can contact us at support@example.com.")
elif "help" in query:
    print("Response: I am here to assist you with your queries.")
else:
    print("Response: Sorry, I could not understand your query.")
