from flask import Flask, send_from_directory
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('', 'index.html')

TOKEN = "7940474487:AAF5RMAv87xMCCzxFIk7WzFwmDTNgz-inXk"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("📸 Включить камеру", web_app=WebAppInfo(url="https://camera11.onrender.com"))
    markup.add(button)
    bot.send_message(message.chat.id, "Открываем встроенное приложение", reply_markup=markup)


@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    """ Получение фото из WebApp """
    photo_data = message.web_app_data.data
    photo_bytes = BytesIO(base64.b64decode(photo_data.split(",")[1]))

    bot.send_photo(message.chat.id, photo_bytes, caption="Вот ваше фото! 📷")


bot.polling(none_stop=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
