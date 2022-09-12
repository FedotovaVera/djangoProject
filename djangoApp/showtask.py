import sqlite3
from djangoApp import datemanager


class ShowTask:
    def __init__(self):
        self.date_task = self.date_task()
        self.time_task = self.time_task()
        self.task_name = self.task_name()

    def task(self):
        db = sqlite3.connect('C:\\Users\\Дом\\PycharmProjects\\djangoProject\\db.sqlite3')
        cur = db.cursor()
        dm = datemanager.DateManager()
        week_start = dm.week_start()
        week_end = dm.week_end()
        request = 'select * from tasks where date_task between ' + "'" + str(week_start) + "'" + ' and ' + "'" + str(
            week_end) + "'"
        sel = cur.execute(request).fetchall()
        return sel

    def date_task(self):
        sel = self.task()
        cnt = len(sel)
        res = []
        for i in range(cnt):
            res.append(sel[i][6])
        return res

    def time_task(self):
        sel = self.task()
        time_task = sel[0][7]
        return time_task

    def task_name(self):
        sel = self.task()
        task_name = sel[0][2]
        return task_name
