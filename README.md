WhatsApp Bakery Order Bot

A WhatsApp bot that lets a small bakery take orders automatically — no one has to sit and reply to every customer message.

What it does
Greets customers and shows a menu (hi / hello)
Displays available cakes and prices (menu)
Takes and confirms orders (order)
Lets customers check order status (status)


Tech used
Python, Flask
Twilio WhatsApp API
ngrok (for local testing)


How to run it:
Install requirements: pip install -r requirements.txt
Run the server: python app.py
Expose it locally with ngrok: ngrok http 5000
Connect the ngrok URL to Twilio's WhatsApp sandbox (or a deployed number)
