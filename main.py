import feedparser
from telegram import Bot
import time
import os

# --- CONFIG ---
RSS_URL = os.environ.get('RSS_URL')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = "@YourChannelUsername"  # or channel ID like -1001234567890
CHECK_INTERVAL = 600  # 10 minutes
posted_guids = set()

bot = Bot(token=BOT_TOKEN)

print("Bot started. Monitoring RSS feed...")

while True:
    feed = feedparser.parse(RSS_URL)
    for entry in feed.entries:
        if entry.guid not in posted_guids:
            message = f"{entry.title}\n{entry.link}"
            bot.send_message(chat_id=CHAT_ID, text=message)
            posted_guids.add(entry.guid)
            print(f"Posted: {entry.title}")
    time.sleep(CHECK_INTERVAL)
