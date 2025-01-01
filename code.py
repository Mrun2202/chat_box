# Define the chatbot class
class SimpleChatbot:
    def __init__(self):
        # Predefined patterns and responses
        self.responses = [
            (r"my name is (.+)", "Hello {0}, how can I assist you today?"),
            (r"hi|hey|hello", "Hello! How can I help you?"),
            (r"what is your name\?", "I am a chatbot created to assist you. You can call me Chatbot."),
            (r"how are you\?", "I'm a bot, so I don't have feelings, but I'm here to help you!"),
            (r"can you help me with (.+)", "Sure, I can help you with {0}. Please provide more details."),
            (r"sorry (.+)", "It's okay. How can I assist you?"),
            (r"thank you|thanks", "You're welcome!"),
            (r"quit", "Bye! Have a great day!"),
        ]

    def respond(self, user_input):
        # Check each pattern and provide the appropriate response
        for pattern, response in self.responses:
            match = re.match(pattern, user_input, re.IGNORECASE)
            if match:
                if "{0}" in response:
                    return response.format(match.group(1))
                return response
        # Default response if no patterns match
        return "I'm sorry, I don't understand that. Can you rephrase?"

# Function to chat with the bot
def chat_with_bot():
    print("Hi, I'm your chatbot. Type 'quit' to exit.")
    chatbot = SimpleChatbot()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start chatting with the bot
if __name__ == "__main__":
    chat_with_bot()
