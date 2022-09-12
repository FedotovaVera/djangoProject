import sqlite3
import datemanager

db = sqlite3.connect('C:\\Users\\Дом\\PycharmProjects\\djangoProject\\db.sqlite3')
cur = db.cursor()
week_start = datemanager.week_start()
week_end = datemanager.week_end()
request = 'select * from tasks where date_task between ' + "'" + str(week_start) + "'" + ' and ' + "'" + str(
    week_end) + "'"
cnt = cur.execute(request).fetchall()
print(cnt)
