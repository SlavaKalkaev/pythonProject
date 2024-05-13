import mysql.connector
import telebot

bot = telebot.TeleBot('7183045578:AAGi3keQJOaZrkOEB-hjTEHmueKAu0WyjJc')

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='slava360',
    port="3306",
    database='MyDB'
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM CHEK")
results = cursor.fetchall()
