import pyautogui
import time

# Function to send a WhatsApp message
def send_whatsapp_message(message, count):
    # Open WhatsApp Web in your browser and ensure the chat is open
    for _ in range(count):
        pyautogui.typewrite(message)  # Type the message
        pyautogui.press("enter")      # Press Enter to send
        time.sleep(0.3)                 # Wait for 1 second

# Message to send
message = "Hey Bro Faheem kesa he ?"
# Number of messages to send
message_count = 100

# Give yourself some time to open WhatsApp Web and select the chat
print("You have 10 seconds to switch to WhatsApp Web and open the chat...")
time.sleep(10)

# Send the message
send_whatsapp_message(message, message_count)

print("Messages sent.")
