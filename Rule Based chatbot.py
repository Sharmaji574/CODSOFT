def chatbot():
    print("Hello! I'm a simple Rule Based ChatBot To assist You. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! Thanks for asking.")
        elif "your name" in user_input:
            print("Chatbot: I'm a rule-based chatbot, here to assist you!")
        elif "time" in user_input:
            from datetime import datetime
            print("Chatbot: The current time is", datetime.now().strftime("%H:%M:%S"))
        elif "date" in user_input:
            from datetime import datetime
            print("Chatbot: Today's date is", datetime.now().strftime("%Y-%m-%d"))
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that. Can you try asking something else?")

# Run the chatbot
chatbot()
