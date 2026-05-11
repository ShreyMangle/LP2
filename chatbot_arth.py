def get_response(user_input):
    # Convert input to lowercase to make it case-insensitive
    user_input = user_input.lower()

    # Rule-Based Response Dictionary (Keywords : Responses)
    # This is the "Knowledge Base" of the chatbot
    responses = {
        "hello": "Hello! Welcome to Cafe Bot. How can I help you today?",
        "hi": "Hi there! Looking for some coffee or snacks?",
        "menu": "We have Espresso, Latte, Cappuccino, and fresh Croissants.",
        "price": "Our coffees range from $3 to $5, and pastries are $4.",
        "hours": "We are open from 8:00 AM to 8:00 PM every day.",
        "location": "You can find us at 123 AI Street, Tech City.",
        "bye": "Goodbye! Have a caffeinated day!",
        "thanks": "You're very welcome!",
        "order": "To place an order, please visit our counter or use our mobile app."
    }

    # Search for keywords in the user's input
    # We use a manual loop to find if any keyword exists in the user's sentence
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]

    # Default response if no keywords match
    return "I'm sorry, I didn't quite understand that. Could you ask about our menu, hours, or location?"

# --- 2. Main Function (User Interaction) ---
def main():
    print("--- Elementary Customer Support Chatbot ---")
    print("(Type 'bye' to exit the chat)\n")

    while True:
        # Get input from the user
        user_text = input("You: ")
        
        # Check for exit condition
        if user_text.lower() == "bye":
            print("Bot:", get_response("bye"))
            break
            
        # Get and print the bot's response
        response = get_response(user_text)
        print("Bot:", response)

# Run the chatbot
if __name__ == "__main__":
    main()