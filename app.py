from pyrogram import Client, filters
import os

# ===== CONFIG =====
API_ID = int(os.environ.get("API_ID", 21189715))   # my.telegram.org se
API_HASH = os.environ.get("API_HASH", "988a9111105fd2f0c5e21c2c2449edfd")       # my.telegram.org se
STRING_SESSION = os.environ.get("STRING_SESSION", "BQCT9g8AhIvbW7Ykc0PcRI_O9SUtiQ3usiayle5J2r0eJVnH8AOJt_dThEvgDA1FCaaDCg_jph0SErj05j78GNhPnlIloVVglljTmREqh-MuUTneJh4e_m23kGUnbCnm2r4d0gDdjlcDOkXiPIlyzIHVerFkwySxNgKGlmt0YsZuCNnlS_qb95vyyuC3Vy7SzPV61ejnIUpghL2VU7u4gYiljErdrSLeDXok5A8CbUVVr2ooRBEoJopZUj6ESXAUD-lPdDGQUil5RIuJUVgvAKVHe_HPylBbjDGxm6ES0r8We0wkT7JIETzaZZ2dho7A8PJNi7eElmPMLwyg2iPnqi0xTQA5cQAAAAGurtJ3AA")  # apna string session yahan daal

SOURCE_CHANNEL = int(os.environ.get("SOURCE_CHANNEL", "-1001234567890"))  # jahan se uthana hai
TARGET_CHANNEL = int(os.environ.get("TARGET_CHANNEL", "-1009876543210"))  # jahan bhejna hai

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
