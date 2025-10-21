import feedparser
import requests
import time
import os

# --- CONFIG ---
RSS_URL = os.environ.get('RSS_URL')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')  # your private or public channel
CHECK_INTERVAL = 600  # 10 minutes
posted_guids = set()

print("Bot started. Monitoring RSS feed...")

while True:
    feed = feedparser.parse(RSS_URL)
    for entry in feed.entries:
        if entry.guid not in posted_guids:
            message = f"{entry.title}\n{entry.link}"
            # Send to Telegram
            requests.get(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                params={"chat_id": CHAT_ID, "text": message}
            )
            posted_guids.add(entry.guid)
            print(f"Posted: {entry.title}")
    time.sleep(CHECK_INTERVAL)
