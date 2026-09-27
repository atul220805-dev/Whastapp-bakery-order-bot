from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_message = request.form.get('Body', '').lower().strip()
    
    response = MessagingResponse()
    reply = response.message()

    if incoming_message in ['hi', 'hello', 'hey']:
        reply.body(
            "🎂 Welcome to Priya's Bakery!\n\n"
            "Type:\n"
            "1️⃣ menu - to see our cakes\n"
            "2️⃣ order - to place an order\n"
            "3️⃣ status - to check your order"
        )

    elif incoming_message == 'menu':
        reply.body(
            "🍰 Our Menu:\n\n"
            "1. Chocolate Truffle - Rs.650\n"
            "2. Butterscotch - Rs.550\n"
            "3. Red Velvet - Rs.750\n"
            "4. Vanilla - Rs.500\n\n"
            "Type 'order' to place yours!"
        )

    elif incoming_message == 'order':
        reply.body(
            "📝 Please type your order like this:\n\n"
            "ORDER: [cake name], [date], [your name]\n\n"
            "Example:\n"
            "ORDER: Red Velvet, 25 April, Atul"
        )

    elif incoming_message.startswith('order:'):
        details = incoming_message.replace('order:', '').strip()
        reply.body(
            f"✅ Order Confirmed!\n\n"
            f"Details: {details}\n\n"
            f"Payment link coming shortly.\n"
            f"Baker will confirm within 1 hour.\n\n"
            f"Thank you for ordering! 🎂"
        )

    elif incoming_message == 'status':
        reply.body(
            "🔍 Your order is being prepared 👩‍🍳\n"
            "Delivery: as per your order date.\n\n"
            "Questions? Reply here anytime!"
        )

    else:
        reply.body(
            "🤖 Didn't catch that!\n"
            "Type 'hi' to see the menu."
        )

    return str(response), 200, {'Content-Type': 'text/xml'}

if __name__ == '__main__':
    app.run(debug=True)