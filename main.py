import feedparser
from telegram import Bot
import asyncio
import os

RSS_URL = os.environ.get('RSS_URL')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')  # private or public
CHECK_INTERVAL = 600
posted_guids = set()

bot = Bot(token=BOT_TOKEN)

async def main():
    print("Bot started. Monitoring RSS feed...")
    while True:
        feed = feedparser.parse(RSS_URL)
        for entry in feed.entries:
            if entry.guid not in posted_guids:
                message = f"{entry.title}\n{entry.link}"
                await bot.send_message(chat_id=CHAT_ID, text=message)
                posted_guids.add(entry.guid)
                print(f"Posted: {entry.title}")
        await asyncio.sleep(CHECK_INTERVAL)

asyncio.run(main())
