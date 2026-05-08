print("Chatbot: Hello! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["bye", "exit", "quit"]:
        print(" Chatbot: Goodbye! ")
        break

    elif user_input in ["hi", "hello", "hey"]:
        print(" Chatbot: Hello! How can I help you?")

    elif "name" in user_input:
        print(" Chatbot: I am your rule-based chatbot.")

    elif "help" in user_input:
        print(" Chatbot: I can answer simple questions.")

    elif "time" in user_input:
        from datetime import datetime
        print(" Chatbot: Current time is", datetime.now().strftime("%H:%M:%S"))

    else:
        print("Chatbot: Sorry, I don’t understand that.")