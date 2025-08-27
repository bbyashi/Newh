from pyrogram import Client, filters
import os

API_ID = int(os.environ.get("API_ID", 21189715))
API_HASH = os.environ.get("API_HASH", "988a9111105fd2f0c5e21c2c2449edfd")
STRING_SESSION = os.environ.get("STRING_SESSION", "BQFDVFMAosp7h7m71HndLeHdic4i2sPJWupjbzugbVAMGl2M7ctBP79d4yW1D7xcI9A3usSguKBf4viUEj3cyJk9YTgKoe3qgnV7eTd8fgN78Bd7JvD5BE8Trtumq3H6zgqGSELAEl3sBPEsqIElN6T5Qu8JYhPMP6NttkAvbQyvmVA7M25T3MABzxYcV79ddPBtpGRSlq3wZzXmBF1n9ZKiLlDsxbyeMT2ZsWWhpzyHqHiI8UHJIm-04q4xQgqB2QyOT56NRJao6qr6jl313RpgmJZGrw7RMjwKC_-Iz2sH6WTSORAgHtA2UUTn4xB2OcvEAdH3w12G2yR7DgTt4hjKvJ5w9AAAAAHO1dopAA")

SOURCE_CHANNEL = -1002150225736
TARGET_CHANNEL = "@TransactionModules"

app = Client(
    "forward_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

@app.on_message(filters.chat(SOURCE_CHANNEL))
async def forward_all(client, message):
    try:
        print(f"📩 New message {message.id} from {message.chat.id} ({message.chat.title})")
        await message.copy(TARGET_CHANNEL)
        print(f"✅ Copied {message.id} to {TARGET_CHANNEL}")
    except Exception as e:
        print(f"❌ Error while forwarding: {e}")

@app.on_message()
async def debug_all(client, message):
    chat_title = message.chat.title if hasattr(message.chat, "title") else "Private/Unknown"
    print(f"🔎 Seen message {message.id} | from {message.chat.id} ({chat_title})")

print("🚀 Forward Bot Started... (String Session Mode)")
app.run()
