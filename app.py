import os
from pyrogram import Client, filters

# ===== CONFIG =====
API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
SOURCE_CHANNEL = int(os.environ.get("SOURCE_CHANNEL", "-1001234567890"))
TARGET_CHANNEL = int(os.environ.get("TARGET_CHANNEL", "-1009876543210"))

# ===== BOT INIT =====
app = Client(
    "forward_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ===== HANDLER =====
@app.on_message(filters.chat(SOURCE_CHANNEL))
async def forward_to_target(client, message):
    try:
        await message.copy(TARGET_CHANNEL)  # message ko copy karega
        print(f"✅ Forwarded message: {message.id}")
    except Exception as e:
        print(f"❌ Error: {e}")

# ===== START BOT =====
print("🚀 Bot Started...")
app.run()
