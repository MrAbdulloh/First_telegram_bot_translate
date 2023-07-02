from transliterate import to_latin, to_cyrillic
import telebot

TOKEN = ""  # This is a token place
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "HELLO")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        result = to_cyrillic(msg)
    else:
        result = to_latin(msg)
    bot.reply_to(message, result)


bot.infinity_polling()
