
from telebot import types

from init import bot, func


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    pokup = types.KeyboardButton('Вход как покупатель')
    prod = types.KeyboardButton('Вход как продавец')
    markup.add(pokup, prod)
    bot.send_message(message.chat.id, "", reply_markup=markup)
    bot.register_message_handler(message, func)