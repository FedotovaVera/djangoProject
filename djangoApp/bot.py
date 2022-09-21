import telebot
import requests
import translators

API_key = '5623471620:AAFIDDb2ZgnxckPENindWH14PVnHAr7pp1Y'

bot = telebot.TeleBot(API_key)

@bot.message_handler(commands=['start'])
def get_command(message):
    bot.send_message(message.chat.id, 'Введите логин и пароль в формате: login@password')

@bot.message_handler(commands=['show'])
def send_kb(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    btn1 = telebot.types.KeyboardButton('ru')
    btn2 = telebot.types.KeyboardButton('en')
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Выберите язык', reply_markup=keyboard)

@bot.message_handler(commands=['close'])
def close_kb(message):
    bot.send_message(message.chat.id, 'Close', reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(content_types=['text'])
def get_message(message):
    try:
        bot.send_message(message.chat.id, message.from_user.first_name + ', Привет' + '\n' + get_weather(message.text) + '\n' + get_advice())
    except ValueError:
        bot.send_message(message.chat.id, 'Такого города нет. попробуйте другой')

def get_weather(city):
    url = 'https://wttr.in/' + city + '?format=3'
    if requests.get(url).status_code == 404:
        raise ValueError
    return requests.get(url).text

def get_advice():
    url = 'https://api.adviceslip.com/advice'
    result = requests.get(url).json()
    return translators.google(result['slip']['advice'], from_language='en', to_language='ru') + '\n' + result['slip']['advice']

bot.polling(none_stop=True)