from pyrogram import Client, filters
import os

# ===== CONFIG =====
API_ID = int(os.environ.get("API_ID", 21189715))
API_HASH = os.environ.get("API_HASH", "988a9111105fd2f0c5e21c2c2449edfd")
STRING_SESSION = os.environ.get("STRING_SESSION", "BQFDVFMAosp7h7m71HndLeHdic4i2sPJWupjbzugbVAMGl2M7ctBP79d4yW1D7xcI9A3usSguKBf4viUEj3cyJk9YTgKoe3qgnV7eTd8fgN78Bd7JvD5BE8Trtumq3H6zgqGSELAEl3sBPEsqIElN6T5Qu8JYhPMP6NttkAvbQyvmVA7M25T3MABzxYcV79ddPBtpGRSlq3wZzXmBF1n9ZKiLlDsxbyeMT2ZsWWhpzyHqHiI8UHJIm-04q4xQgqB2QyOT56NRJao6qr6jl313RpgmJZGrw7RMjwKC_-Iz2sH6WTSORAgHtA2UUTn4xB2OcvEAdH3w12G2yR7DgTt4hjKvJ5w9AAAAAHO1dopAA")

SOURCE_CHANNEL = -1002388199267          # 👈 source private channel ka ID
TARGET_CHANNEL = -1002951284170  # 👈 target public channel ka username

# ===== CLIENT =====
app = Client("forward_bot", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)

# ===== HANDLER =====
@app.on_message(filters.chat(SOURCE_CHANNEL))
async def forward_all(client, message):
    try:
        target = await client.get_chat(TARGET_CHANNEL)   # ✅ resolve every time
        await message.copy(target.id)  # text + photo + video + docs sab jayega
        print(f"✅ Forwarded message {message.id}")
    except Exception as e:
        print(f"❌ Error: {e}")

print("🚀 Forward Bot Started... (String Session Mode)")
app.run()
