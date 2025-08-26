from pyrogram import Client, filters
import os

# ===== CONFIG =====
API_ID = int(os.environ.get("API_ID", 21189715))   # my.telegram.org se
API_HASH = os.environ.get("API_HASH", "988a9111105fd2f0c5e21c2c2449edfd")       # my.telegram.org se
STRING_SESSION = os.environ.get("STRING_SESSION", "BQCT9g8ANBd26gmc7L1A1FAHliYdD1tS-DS6_taE5jMOOZOfHl6UgCLHem7WKqiKcEIPSzGa4cgLz4c0KwDSa5qNwnz6wXmivAHK4EJuRzQAttb5RvmY9tr_IxrKuy9DUQKhQTPdc4qCPuM5PFAoWKwdOCbjK7G5__murs9QjtggEzRo9JqxeIbnoz52eoxlcTdrRYxd1Npg4Bfu3_9cy7LIQQNLxD68VH5_0Zl7oresXFPlo2pNFumm6G85OESPKutWdU_FQzKLVWaKMl-DE7MfryV8T8qRmWg27aixb_pBDeAgG62e_aCDLjrQqT_DTp4-2aaBEzNLScKy83IaUmUA_8-f4gAAAAH3nNugAA")  # apna string session yahan daal

SOURCE_CHANNEL = int(os.environ.get("SOURCE_CHANNEL", "-1002388199267"))  # jahan se uthana hai
TARGET_CHANNEL = int(os.environ.get("TARGET_CHANNEL", "-1002951284170"))  # jahan bhejna hai

# ===== CLIENT =====
app = Client("forward_bot", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)

# ===== HANDLER =====
@app.on_message(filters.chat(SOURCE_CHANNEL))
async def forward_all(client, message):
    try:
        await message.copy(TARGET_CHANNEL)  # ✅ sab kuch copy hoga (media + text)
        print(f"✅ Forwarded message {message.id}")
    except Exception as e:
        print(f"❌ Error: {e}")

print("🚀 Forward Bot Started... (String Session Mode)")
app.run()
