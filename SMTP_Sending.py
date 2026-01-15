import random
import smtplib
from email.message import EmailMessage
import os

# --- CONFIGURARE DATE ---
SENDER_EMAIL = os.environ.get("SENDER_EMAIL").strip()
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD").strip()
# --- RECEIVER EMAILS ---
RECEIVER_EMAIL1 = os.environ.get("RECEIVER_EMAIL1").strip()
RECEIVER_EMAIL2 = os.environ.get("RECEIVER_EMAIL2").strip()
RECEIVER_EMAIL3 = os.environ.get("RECEIVER_EMAIL3").strip()

names = ["The King of Burgers Grigotita-Marius",
         "The Whopper Final Boss Grigorita-Marius",
         "Royal Grill Marius-Master", "Marius's Chef",
         "Hexa Bacon Cheddar Whopper Lord Grigorita-Marius",
         "The King's Morning Feast! Only at WhopperKing!"]
chosen_name = random.choice(names)
# --- CREAREA MESAJULUI ---
msg_1 = EmailMessage()
msg_1['Subject'] = f"👑 {chosen_name} 👑"
msg_1['From'] = SENDER_EMAIL
msg_1['To'] = RECEIVER_EMAIL1
msg_1.set_content("Whopper, Whopper, Whopper! 🍔\n "
                  "Start your day like a King, Marius, "
                  "with a massive Triple Bacon Cheese "
                  "Whopper paired with our famous large "
                  "fries and an ice-cold drink! 🥓🍟🥤 \n"
                  "Claim this royal feast now and we’ll even "
                  "throw in a free side of golden onion rings "
                  "if you order in the next 20 minutes! 👑✨ \n"
                  "Don't wait—have it your way right away! 🏃‍♂️💨")
msg_2 = EmailMessage()
msg_2['Subject'] = f"👑 {chosen_name} 👑"
msg_2['From'] = SENDER_EMAIL
msg_2['To'] = RECEIVER_EMAIL2
msg_2.set_content("Whopper, Whopper, Whopper! 🍔\n "
                  "Start your day like a King, Marius, "
                  "with a massive Triple Bacon Cheese "
                  "Whopper paired with our famous large "
                  "fries and an ice-cold drink! 🥓🍟🥤 \n"
                  "Claim this royal feast now and we’ll even "
                  "throw in a free side of golden onion rings "
                  "if you order in the next 20 minutes! 👑✨ \n"
                  "Don't wait—have it your way right away! 🏃‍♂️💨")
msg_3 = EmailMessage()
msg_3['Subject'] = f"👑 {chosen_name} 👑"
msg_3['From'] = SENDER_EMAIL
msg_3['To'] = RECEIVER_EMAIL3
msg_3.set_content("Whopper, Whopper, Whopper! 🍔\n "
                  "Start your day like a King, Marius, "
                  "with a massive Triple Bacon Cheese "
                  "Whopper paired with our famous large "
                  "fries and an ice-cold drink! 🥓🍟🥤 \n"
                  "Claim this royal feast now and we’ll even "
                  "throw in a free side of golden onion rings "
                  "if you order in the next 20 minutes! 👑✨ \n"
                  "Don't wait—have it your way right away! 🏃‍♂️💨 \n"
                  "\n Daca bagi in spam ori dai mute la gmail esti pidar <3")
# --- TRIMITEREA ---
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print("Autentificare...")
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg_1)
    server.send_message(msg_2)
    server.send_message(msg_3)
    server.quit()
    print("✅ SUCCES! Email-ul a fost trimis.")
except Exception as e:
    print(f"❌ Eroarea este: {e}")