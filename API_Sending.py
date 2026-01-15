import os
import requests
import random

# Listă de nume pentru expeditor
names = ["The King of Burgers Grigotita Marius", "The Whopper Final Boss Grigorita Marius", "Royal Grill Marius-Master", "Marius's Chef"]

API_KEY = os.environ.get("BREVO_API_KEY")
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")

chosen_name = random.choice(names)
url = "https://api.brevo.com/v3/smtp/email"

payload = {
    "sender": {"name": chosen_name, "email": SENDER_EMAIL},
    "to": [{"email": RECEIVER_EMAIL}],
    "subject": f"👑 Hi, {chosen_name}! 👑",
    "htmlContent": "<h1>Whopper Time!</h1><p>Burgerul tau e gata.</p>"
}

payload = {
    "sender": {"name": "WhopperKing", "email": SENDER_EMAIL},
    "to": [{"email": RECEIVER_EMAIL, "name": "Grigorita Marius The Yearly Whopper King!"}],
    "subject": "👑 The King's Morning Feast! 👑",
    "htmlContent": """
        <html>
            <body>
                <h1>Whopper, Whopper, Whopper! 🍔</h1>
                <p>Start your day like a King, Marius!</p>
                <p>Penta Bacon Cheese Whopper with large fries is waiting. 🥓🍟</p>
                <p>And grab some soda for the flavor!</p>
            </body>
        </html>
    """
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "api-key": API_KEY
}

response = requests.post(url, json=payload, headers=headers)
print(f"Status: {response.status_code}")