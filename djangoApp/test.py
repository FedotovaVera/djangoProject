import sqlite3


conn = sqlite3.connect('C:\\Users\\Дом\\PycharmProjects\\djangoProject\\db.sqlite3', check_same_thread=False)
cursor = conn.cursor()

task_name = '1'
task_comment = '1'
date_add = '1'
date_task = '1'
time_task = '1'
user_id_id ='1'

conn.cursor().execute("INSERT INTO djangoapp_tasks (task_name, task_comment, date_add, date_task, time_task, user_id_id VALUES (?,?,?,?,?,?)" , (task_name, task_comment, date_add, date_task, time_task, user_id_id))