import os
import requests
import random

# Listă de nume pentru expeditor
names = ["The King of Burgers Grigotita-Marius",
         "The Whopper Final Boss Grigorita-Marius",
         "Royal Grill Marius-Master", "Marius's Chef",
         "Hexa Bacon Cheddar Whopper Lord Grigorita-Marius"]

API_KEY = os.environ.get("BREVO_API_KEY")
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")

chosen_name = random.choice(names)
url = "https://api.brevo.com/v3/smtp/email"

payload = {
    "sender": {"name": "WhopperKing", "email": SENDER_EMAIL},
    "to": [{"email": RECEIVER_EMAIL, "name": "Grigorita Marius"}],
    "subject": f" {chosen_name} ",
    "textContent": f"""Whopper, Whopper, Whopper! 
Start your day like a King, Marius!
Penta Bacon Cheese Whopper with large fries is waiting.
And grab some soda for the flavor!
"""
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "api-key": API_KEY
}

try:
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print(f"✅ SUCCES! Email-ul a fost trimis cu succes.")
        print(f"ID Mesaj: {response.json().get('messageId')}")
    else:
        print(f"❌ EROARE API: Cod status {response.status_code}")
        print(f"Detalii eroare: {response.text}")

except Exception as e:
    print(f"❌ EROARE CRITICĂ: Nu s-a putut contacta serverul Brevo. Detalii: {e}")