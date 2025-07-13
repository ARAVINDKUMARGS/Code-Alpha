# Rule-Based Chatbot
print("Welcome to CodeAlpha Chatbot! Type 'exit' to end.")

while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
    elif "hello" in user_input:
        print("Chatbot: Hello there!")
    elif "internship" in user_input:
        print("Chatbot: We offer Python, Web Dev and more!")
    elif "thanks" in user_input:
        print("Chatbot: You're welcome!")
    else:
        print("Chatbot: I don't understand.")
