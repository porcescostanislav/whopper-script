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
RECEIVER_EMAIL4 = os.environ.get("RECEIVER_EMAIL4").strip()

names = ["The King of Burgers Grigotita-Marius",
         "The Whopper Final Boss Grigorita-Marius",
         "Royal Grill Marius-Master",
         "Hexa Bacon Cheddar Whopper Lord Grigorita-Marius",
         "The King's Morning Feast! Only at WhopperKing!",
        "The Supreme Architect of BBQ Sauce, Grigorita Marius",
        "The Emperor of Golden Fries and Onion Rings, Marius",
        "Governor of the Bacon & Cheddar Provinces, Marius",
        "Executive President of the Fried Potato Kingdom, Marius",
        "Marius: The Living Legend of the 8 AM Burger",
        "His Majesty, Marius, The Grand Duke of Melted Cheese",
        "The Octa-Bacon Heartbreaker: Marius Morning Edition",
        "The Cheese Apocalypse: Marius Special",
        "The Triple-Threat Whopper for Marius (Bacon, Beef & Glory)",
        "Breakfast of Titans: The Marius Mega-Cheddar Feast",
        "Oceans of Mayo and Mountains of Bacon for Marius",
        "The Penta-Cheese Nuclear Whopper Protocol for Marius",
        "WHOPPER Protocol: Activated for Grigorita Marius",
        "Marius, your burger passed the safety test: It's Delicious!",
        "Code Red: Critical Hunger Levels Detected in Sector Marius",
        "Royal Transmission: The Marius Burger is Ready for Siege!",
        "Survival Instructions for Marius: Open Mail, Devour Whopper",
        "Target Acquired: The Grigorita-Marius Morning Feast",
        "Don’t tell the Salad—The Whopper is here for Marius!",
        "A Message from the Grill: Marius, come and get it!",
        "The Whopper Final Boss has appeared: Grigorita Marius",
        "The Daily Dose of Bacon-Induced Happiness for Marius",
        "Marius, even the King bows to your appetite today!",
        "The Royal Feast of Marius: Penta-Bacon Edition",
        "Marius, the Grill Master has prepared your morning Whopper"
        ]

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
msg_4 = EmailMessage()
msg_4['Subject'] = f"👑 {chosen_name} 👑"
msg_4['From'] = SENDER_EMAIL
msg_4['To'] = RECEIVER_EMAIL3
msg_4.set_content("Whopper, Whopper, Whopper! 🍔\n "
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
    server.send_message(msg_4)
    server.quit()
    print("✅ SUCCES! Email-ul a fost trimis.")
except Exception as e:
    print(f"❌ Eroarea este: {e}")