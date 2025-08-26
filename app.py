from pyrogram import Client, filters
import os

# ===== CONFIG =====
API_ID = int(os.environ.get("API_ID", 12345))   # my.telegram.org se
API_HASH = os.environ.get("API_HASH", "")       # my.telegram.org se

SOURCE_CHANNEL = int(os.environ.get("SOURCE_CHANNEL", "-1001234567890"))  # jahan se uthana hai
TARGET_CHANNEL = int(os.environ.get("TARGET_CHANNEL", "-1009876543210"))  # jahan bhejna hai

# ===== USER SESSION =====
app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

# ===== HANDLER =====
@app.on_message(filters.chat(SOURCE_CHANNEL))
async def forward_all(client, message):
    try:
        # ✅ poora message (media/text sab) copy hoga
        await message.copy(TARGET_CHANNEL)
        print(f"✅ Forwarded message {message.id}")
    except Exception as e:
        print(f"❌ Error: {e}")

print("🚀 Forward Bot Started... (media + text sab forward hoga)")
app.run()
