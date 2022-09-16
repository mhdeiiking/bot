import requests,re,telebot
import time
from time import sleep 
bot = telebot.TeleBot("5776886346:AAGWJ36x2SZFqmi5OIT-tQNW_AV6Zj-Wqio")

r = (requests.get("https://download.quranicaudio.com/quran/mishaari_raashid_al_3afaasee/").text)
@bot.channel_post_handler(commands=['start'])
def start(message):
    for i in range(0,114):
        a = (re.findall('<a href="(.*?).mp3">(.*?).mp3</a>',r)[i][i])
        print(a)
        bot.send_audio(message.chat.id,audio=f"https://download.quranicaudio.com/quran/mishaari_raashid_al_3afaasee/001.mp3",caption="استغفرالله .")
        sleep(6)
    bot.send_message(message.chat.id,f"انتهى النشر .")
bot.infinity_polling()
