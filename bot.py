from pyrogram import Client, filters
app = Client(
  "FuckYjeueuou",
  api_id = 9398500,
  api_hash = "ad2977d673006bed6e5007d953301e13",
  bot_token = "5776886346:AAHA-WOxRU_ODu5EnGl22oouqICHQBfmoD0"
)
@app.on_message(filters.media & filters.private)
def test(client, message):
  try:
    location = "./github/workflows"
    x = message.download(location)
    print(x)
    message.reply("done")
  except Exception as e:
    print(e)


app.run()
