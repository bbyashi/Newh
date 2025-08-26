from pyrogram import Client, filters
import os

# ===== CONFIG =====
API_ID = int(os.environ.get("API_ID", 21189715))
API_HASH = os.environ.get("API_HASH", "988a9111105fd2f0c5e21c2c2449edfd")
STRING_SESSION = os.environ.get("STRING_SESSION", "BQCT9g8AOdnpXHzXUcmYLeFogKEFsm0-yPQcAxDBSEDqs0l4T5TEwiGKqH-a5P6U7awUj40drtEVj24EhOQfQyOPfsyIHXkXIb2DvZHuux9aS6BXEZk2UGiLvMDASkuUifF1ua0ilT1kMw6jeXk8zyMk2sQTKxiW66A3v_KklAYdn6wSeJswDXpONC7zXAm8W9i7VeHBO0a6IrfQbRhqj17Qo9NICoo_QkuwI-G7cno8eT5ruBU1VknnNLBHOSJ_zLBOtDGQN0n3Mz-vSBwZRLGlfjHQSbcYKLgghrlTRP8QoxJbxaKRl2E68-csWDTk7aJiC3GQoFib75n4T-JqcPmqmAIRAQAAAAHO1dopAA")

SOURCE_CHANNEL = -1002388199267          # 👈 source private channel ka ID
TARGET_CHANNEL = "@TransactionModules"  # 👈 target public channel ka username

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
