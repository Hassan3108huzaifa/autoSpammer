# first install `pip install pyautogui`

import pyautogui
import time

def send_whatsapp_message(message, count):
    
    for _ in range(count):
        pyautogui.typewrite(message) 
        pyautogui.press("enter")      
        time.sleep(1) # Wait for 1 second


message = "Hey Bro Faheem kesa he ?"

message_count = 100


print("You have 10 seconds to switch to WhatsApp Web and open the chat...")
time.sleep(10)


send_whatsapp_message(message, message_count)

print("Messages sent.")
