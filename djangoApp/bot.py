from datetime import date, timedelta
import telebot
import sqlite3
from djangoApp import datemanager

API_key = '5623471620:AAFIDDb2ZgnxckPENindWH14PVnHAr7pp1Y'

bot = telebot.TeleBot(API_key)
conn = sqlite3.connect('C:\\Users\\Дом\\PycharmProjects\\djangoProject\\db.sqlite3', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_name: str):
    sql = "select last_name from auth_user where last_name=:user_name"
    sel = conn.cursor().execute(sql, {"user_name": user_name}).fetchall()
    if len(sel) != 0:
        return 1
    else:
        return 0


def db_tasks(user_name: str, date_day1: date, date_day2: date):
    sql = "SELECT time_task, task_name, date_task FROM djangoapp_tasks t join auth_user u on u.id=t.user_id_id where last_name=:user_name and date_task between :date_task1 and :date_task2 and date_end='' order by date_task, time_task"
    tasks = conn.cursor().execute(sql,
                                  {"user_name": user_name, "date_task1": date_day1, "date_task2": date_day2}).fetchall()
    return tasks


@bot.message_handler(commands=['start'])
def get_command(message):
    if db_table_val(message.from_user.username) == 1:
        bot.send_message(message.chat.id,
                         message.from_user.first_name + ' , добро пожаловать! \n Доступные команды: \n /task_today - задачи на сегодня \n /task_tomorrow - задачи на завтра \n /task_week - задачи на неделю')
        sql = "update auth_user set email=:id where last_name=:user_name"
        conn.cursor().execute(sql, {"user_name": message.from_user.username, "id": message.chat.id})
        conn.commit()
    else:
        bot.send_message(message.chat.id,
                         message.from_user.first_name + ', тебе необходимо зарегистрироваться на сайте')


@bot.message_handler(commands=['task_today'])
def get_command(message):
    tasks = db_tasks(message.from_user.username, date.today(), date.today())
    task = ''
    if db_table_val(message.from_user.username) == 1 and len(tasks) != 0:
        for l in range(len(tasks)):
            task += str(l + 1) + '. ' + tasks[l][0] + ': ' + tasks[l][1] + '\n'
        bot.send_message(message.chat.id,
                         message.from_user.first_name + ' , твои задания на сегодня: ' + '\n' + str(task))
    elif db_table_val(message.from_user.username) == 1 and len(tasks) == 0:
        bot.send_message(message.chat.id, message.from_user.first_name + ' , на сегодня не установлено задач')
    else:
        bot.send_message(message.chat.id,
                         message.from_user.first_name + ', тебе необходимо зарегистрироваться на сайте')


@bot.message_handler(commands=['task_tomorrow'])
def get_command(message):
    dt = date.today() + timedelta(days=1)
    tasks = db_tasks(message.from_user.username, dt, dt)
    if db_table_val(message.from_user.username) == 1 and len(tasks) != 0:
        task = ''
        for l in range(len(tasks)):
            task += str(l + 1) + '. ' + tasks[l][0] + ': ' + tasks[l][1] + '\n'
        bot.send_message(message.chat.id,
                         message.from_user.first_name + ' , твои задания на завтра: ' + '\n' + str(task))
    elif db_table_val(message.from_user.username) == 1 and len(tasks) == 0:
        bot.send_message(message.chat.id, message.from_user.first_name + ' , на завтра не установлено задач')
    else:
        bot.send_message(message.chat.id,
                         message.from_user.first_name + ', тебе необходимо зарегистрироваться на сайте')


@bot.message_handler(commands=['task_week'])
def get_command(message):
    date1 = datemanager.DateManager().day_monday
    date2 = datemanager.DateManager().day_sunday
    tasks = db_tasks(message.from_user.username, date1, date2)
    if db_table_val(message.from_user.username) == 1 and len(tasks) != 0:
        task = ''
        for l in range(len(tasks)):
            task += tasks[l][2] + '. ' + tasks[l][0] + ': ' + tasks[l][1] + '\n'
        bot.send_message(message.chat.id,
                         message.from_user.first_name + ' , твои задания на неделю: ' + '\n' + str(task))
    elif db_table_val(message.from_user.username) == 1 and len(tasks) == 0:
        bot.send_message(message.chat.id, message.from_user.first_name + ' , на текущую неделю не установлено задач')
    else:
        bot.send_message(message.chat.id,
                         message.from_user.first_name + ', тебе необходимо зарегистрироваться на сайте')


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/add_task':
        bot.send_message(message.from_user.id, "Введи название задачи")
        bot.register_next_step_handler(message, get_task_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')


def get_task_name(message):
    if message.text == '/end':
        pass
    else:
        global task_name
        task_name = message.text
        bot.send_message(message.from_user.id, 'Введи описание задачи')
        bot.register_next_step_handler(message, get_comment)


def get_comment(message):
    global task_comment
    task_comment = message.text
    bot.send_message(message.from_user.id, 'Введи дату задачи в формате гггг-мм-дд')
    bot.register_next_step_handler(message, get_date)


def get_date(message):
    global date_task
    date_task = message.text
    bot.send_message(message.from_user.id, 'Введи время задачи в формате чч:мм')
    bot.register_next_step_handler(message, get_time)


def get_time(message):
    global time_task
    time_task = message.text
    bot.send_message(message.from_user.id, 'Проверь данные: ' + '\n' + 'Название:' + '\n' + task_name +
                     '\n' + 'Описание:' + '\n' + task_comment +
                     '\n' + 'Дата:' + '\n' + date_task +
                     '\n' + 'Время:' + '\n' + time_task + '\n' + '\n' +
                     'Данные верны? (Ответь "Да" или "Нет")')
    bot.register_next_step_handler(message, get_correct)


def get_correct(message):
    global correct_task
    correct_task = message.text
    if message.text == 'Да':
        bot.send_message(message.from_user.id, 'Данные внесены успешно')
        date_add = date.today().strftime("%Y-%m-%d")
        sql_id = "select id from auth_user where last_name=:user_name"
        user_id_id = conn.cursor().execute(sql_id, {"user_name": message.from_user.username}).fetchall()[0][0]
        conn.cursor().execute(
            "INSERT INTO djangoapp_tasks (task_name, task_comment, date_add, date_task, time_task, user_id_id, date_end) VALUES (?,?,?,?,?,?,?)",
            (task_name, task_comment, date_add, date_task, time_task, int(user_id_id), ''))
        conn.commit()
    elif message.text == 'Нет':
        bot.send_message(message.from_user.id, "Введи название задачи. \nДля выхода нажми /end ")
        bot.register_next_step_handler(message, get_task_name)


bot.polling(none_stop=True)
