def chatbot():
    print("Bot: Namaste! I'm your assistant. Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()

        if "hello" in user or "hi" in user or "namaste" in user:
            print("Bot: Hello! How can I help you today?")
        elif "price" in user:
            print("Bot: Please tell me which product you're asking about.")
        elif "product" in user:
            print("Bot: We offer laptops, phones, and headphones.")
        elif "laptop" in user:
            print("Bot: Our laptops start at ₹65,000 with 8GB RAM and SSD storage.")
        elif "phone" in user:
            print("Bot: Phones are available from ₹20,000 onwards.")
        elif "headphone" in user or "headphones" in user:
            print("Bot: Headphones cost ₹4,999 and have noise cancellation.")
        elif "order" in user:
            print("Bot: Please provide your order ID to check the delivery status.")
        elif "return" in user or "refund" in user:
            print("Bot: You can request a return or refund within 7 days of delivery.")
        elif "thank" in user:
            print("Bot: You're welcome! Happy to help 😊")
        elif "bye" in user or "exit" in user:
            print("Bot: Goodbye! Have a great day 👋")
            break
        else:
            print("Bot: Sorry, I didn't get that. Can you please rephrase?")

chatbot()
