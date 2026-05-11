# Hospital Rule-Based Chatbot

print("===== HOSPITAL CHATBOT =====")

while True:

    print("\nEnter your symptoms separated by comma")
    print("Example: fever, headache")
    print("Type 'exit' to stop")

    user_input = input("\nYou: ").lower()

    # Exit
    if user_input == "exit":

        print("\nChatbot: Stay healthy. Goodbye!")
        break

    # Convert symptoms into list
    symptoms = user_input.split(",")

    # Remove spaces
    symptoms = [s.strip() for s in symptoms]

    # Rules with multiple conditions

    if "fever" in symptoms and "headache" in symptoms:

        print("\nChatbot: You might be having Dengue or Viral Fever.")
        print("Recommended Doctor: Dr. Sharma")
        print("Medicine: Paracetamol")
        print("Advice: Drink plenty of fluids.")

    elif "cough" in symptoms and "fever" in symptoms:

        print("\nChatbot: You may have Flu.")
        print("Recommended Doctor: Dr. Singh")
        print("Medicine: Cough Syrup + Rest")

    elif "stomach pain" in symptoms and "vomiting" in symptoms:

        print("\nChatbot: You may have Food Poisoning.")
        print("Recommended Doctor: Dr. Patel")
        print("Medicine: Antacid")

    elif "headache" in symptoms:

        print("\nChatbot: You may have Migraine.")
        print("Recommended Doctor: Dr. Gupta")
        print("Medicine: Ibuprofen")

    elif "cough" in symptoms:

        print("\nChatbot: You may have Common Cold.")
        print("Recommended Doctor: Dr. Singh")
        print("Medicine: Cough Syrup")

    else:

        print("\nChatbot: Sorry, disease not identified.")
        print("Please consult a specialist.")