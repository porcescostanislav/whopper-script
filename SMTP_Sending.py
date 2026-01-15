import random
import smtplib
from email.message import EmailMessage
from time import sleep
import os

# --- CONFIGURARE DATE ---
SENDER_EMAIL = os.environ.get("SENDER_EMAIL").strip()
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD").strip()
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL").strip()

names = ["The King of Burgers Grigotita-Marius",
         "The Whopper Final Boss Grigorita-Marius",
         "Royal Grill Marius-Master", "Marius's Chef",
         "Hexa Bacon Cheddar Whopper Lord Grigorita-Marius",
         "The King's Morning Feast! Only at WhopperKing!"]
chosen_name = random.choice(names)
# --- CREAREA MESAJULUI ---
msg = EmailMessage()
msg['Subject'] = f"👑 {chosen_name} 👑"
msg['From'] = SENDER_EMAIL
msg['To'] = RECEIVER_EMAIL
msg.set_content("Whopper, Whopper, Whopper! 🍔\n Start your day like a King, Marius, with a massive Triple Bacon Cheese Whopper paired with our famous large fries and an ice-cold drink! 🥓🍟🥤 \nClaim this royal feast now and we’ll even throw in a free side of golden onion rings if you order in the next 20 minutes! 👑✨ \nDon't wait—have it your way right away! 🏃‍♂️💨")
# --- TRIMITEREA ---
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print("Autentificare...")
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()
    print("✅ SUCCES! Email-ul a fost trimis.")

except Exception as e:
    print(f"❌ Eroarea este: {e}")