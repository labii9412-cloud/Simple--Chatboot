"""
Task: Build a simple rule-based chatbot.
Key concepts: if-elif, functions, loops, input/output
"""

def get_response(user_input):
    text = user_input.lower().strip()

    if "hello" in text or "hi" in text:
        return "Hi!"
    elif "how are you" in text:
        return "I'm fine, thanks!"
    elif "bye" in text:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."


def run_chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    run_chatbot()