from telebot import types

from init import bot, cursor


@bot.message_handler(content_types=['text'])
def available(message):
    if message.text == "Проверить наличие товара":
        m = "Введите наименование товара в виде (Товар,бренд)"
        bot.send_message(message.chat.id, m)
        msg = bot.register_message_handler()
        if msg in cursor.execute("SELECT * FROM Availability"):
            bot.send_message(message.chat.id, "Деталь доступна к покупке")
        else:
            bot.send_message(message.chat.id, "Детали нет в наличии")


@bot.message_handler(content_types=['text'])
def listOfShop(message):
    if message.text == "Список магазинов":
        cursor.execute("SELECT * FROM Shop")
        bot.send_message(message.chat.id, cursor.fetchall())


@bot.message_handler(content_types=['text'])
def website(message):
    if message.text == "Посетить вебсайт":
        mark = types.InlineKeyboardMarkup()
        mark.add(types.InlineKeyboardButton("Посетить вебсайт", url='https://kickscootershop.ru'))
        bot.send_message(message.chat.id, "перейдите на сайт", reply_markup=mark)


@bot.message_handler(content_types=['text'])
def partInBucket(message):
    ms = bot.register_message_handler()
    list = []
    if message.text == "Добавить товар в избранное":
        if available(ms):
            list.append(ms)
            text = "Товар успешно добавлен"
            bot.send_message(message.chat.id, text)
        else:
            tex = "Товара нет в наличии , его нельзя добавить в корзину"
            bot.send_message(message.chat.id, tex)

@bot.message_handler(content_types=['text'])
def showListOfFav(message):
    if message.text == 'Посмотреть избранные товары':
        bot.send_message(message.chat.id, list)



@bot.message_handler(content_types=['text'])
def historyOfBuy(message):
    if message == "Посмотреть историю покупок":
        cursor.execute("SELECT * FROM CHEK")
        bot.send_message(message.chat.id, cursor.fetchall())

@bot.message_handler(content_types=['text'])
def addPartToAvailability(message):
    if message == "Добавить товар в ассортимент":
        bot.send_message(message.chat.id,"Введите наименование товара")
        name = bot.register_message_handler()
        bot.send_message(message.chat.id, "Введите бренд товара")
        brand = bot.register_message_handler()
        bot.send_message(message.chat.id, "Введите материал товара")
        material = bot.register_message_handler()
        bot.send_message(message.chat.id, "Введите страну производителя товара")
        country = bot.register_message_handler()
        bot.send_message(message.chat.id, "Введите цену товара")
        cost = bot.register_message_handler()
        bot.send_message(message.chat.id, "Введите кол-во товара")
        count = bot.register_message_handler()
        bot.send_message(message.chat.id, "Введите ссылку на фото товара")
        url = bot.register_message_handler()
        cursor.execute("INSERT INTO Part values(PartID,PartName,PartBrand,PartMaterial,PartCountry,PartCost,PartCount,PartPhotoURL)", (name,brand,material,country,cost,count,url))


