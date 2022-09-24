import time
from collections import Counter
import schedule
from datetime import date, datetime
import telebot
import sqlite3


API_key = '5623471620:AAFIDDb2ZgnxckPENindWH14PVnHAr7pp1Y'

bot = telebot.TeleBot(API_key)
conn = sqlite3.connect('C:\\Users\\Дом\\PycharmProjects\\djangoProject\\db.sqlite3', check_same_thread=False)
cursor = conn.cursor()

def db_reminder_day():
    sql = "select time_task, task_name, date_task, email from djangoapp_tasks t join auth_user u on u.id=t.user_id_id where date_task=:date_task order by u.id, date_task, time_task"
    tasks = conn.cursor().execute(sql, {"date_task": date.today()}).fetchall()
    counter = list()
    for i in range(len(tasks)):
        counter.append(tasks[i][3])
    for id in Counter(counter).keys():
        if id != '':
            task = ''
            for l in range(len(tasks)):
                if tasks[l][3] != '' and id == tasks[l][3]:
                    task += tasks[l][0] + ': ' + tasks[l][1] + '\n'
            bot.send_message(id,
                'Доброе утро! Твои задания на сегодня: ' + '\n' + str(task))



def db_reminder_hour():
    if 6 <= datetime.now().hour <= 21:
        sql = "select time_task, task_name, date_task, email from djangoapp_tasks t join auth_user u on u.id=t.user_id_id where date_task=:date_task and substring(time_task,1,2) between :time1 and :time2 order by u.id, date_task, time_task"
        tasks = conn.cursor().execute(sql, {"date_task": date.today(), "time1": str(datetime.now().hour+1), "time2": str(datetime.now().hour + 4)}).fetchall()
        counter = list()
        for i in range(len(tasks)):
            counter.append(tasks[i][3])
        for id in Counter(counter).keys():
            if id != '':
                task = ''
                for l in range(len(tasks)):
                    if tasks[l][3] != '' and id == tasks[l][3]:
                        task += tasks[l][0] + ': ' + tasks[l][1] + '\n'
                bot.send_message(id,
                    'Напоминание\nДо завершения этих задач осталось менее 3 часов: \n' + str(task))

schedule.every(1).day.at("08:00").do(db_reminder_day)
schedule.every(1).hour.at(":00").do(db_reminder_hour)

while True:
    schedule.run_pending()
    time.sleep(1)