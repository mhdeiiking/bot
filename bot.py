from pyrogram import Client, filters
import asyncio
app = Client(
  "FuckYjeueuou",
  api_id = 9398500,
  api_hash = "ad2977d673006bed6e5007d953301e13",
  bot_token = "5776886346:AAHA-WOxRU_ODu5EnGl22oouqICHQBfmoD0"
)
@app.on_message(filters.media & filters.forwarded)
@app.on_message(filters.media & filters.private)
async def test(client, message):
  try:
    location = "./github/workflows/"
    x = await app.download_media(message,file_name="./github/workflows/app.ipa")
    print(x)
    await app.send_document(message.chat.id,file_name="./github/workflows/app.ipa")
    await message.reply("done")
  except Exception as e:
    print(e)


app.run()
