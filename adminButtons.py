from telebot import types


def admin_markups():
    markups = types.ReplyKeyboardMarkup(reply_markup=True, row_width=3)
    add = types.KeyboardButton('Добавить товар в ассортимент')
    nalichie = types.KeyboardButton('Проверить наличие товара')
    zakaz = types.KeyboardButton('Посмотреть заказы для сбора')
    markups.add(add, nalichie, zakaz)
    return markups