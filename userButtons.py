from telebot import types


def user_markups():
    markup = types.ReplyKeyboardMarkup(reply_markup=True, row_width=3)
    shop = types.KeyboardButton('Список магазинов')
    avail = types.KeyboardButton('Проверить наличие товара')
    website = types.KeyboardButton('Посетить вебсайт')
    bucket = types.KeyboardButton('Добавить товар в избранное')
    history = types.KeyboardButton('Посмотреть историю покупок')
    izbrannoe = types.KeyboardButton('Посмотреть избранные товары')
    markup.add(shop, avail, website, bucket, history,izbrannoe)
    return markup