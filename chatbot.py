def chatbot_response(user_input)

    user_input = user_input.lower()

    # Rules: keyword-based matching
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! How about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a wonderful day!"
    elif "your name" in user_input:
        return "I am RuleBot, your friendly chatbot."
    elif "weather" in user_input:
        return "I can’t check the live weather, but I hope it's sunny where you are!"
    elif "help" in user_input:
        return "Sure! You can ask me about greetings, my name, the weather, or just chat casually."
    else:
        return "I'm not sure I understand. Could you rephrase?"

def run_chatbot():
    print("RuleBot: Hello! I am your chatbot. Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("RuleBot: Goodbye! Have a nice day!")
            break
        response = chatbot_response(user_input)
        print(f"RuleBot: {response}")

if __name__ == "__main__":
    run_chatbot()