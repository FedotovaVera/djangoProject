from datetime import date, timedelta


class DateManager:
    def __init__(self):
        self.day_today = self.day_today()
        self.day_monday = self.day_monday()
        self.day_tuesday = self.day_tuesday()
        self.day_wednesday = self.day_wednesday()
        self.day_thursday = self.day_thursday()
        self.day_friday = self.day_friday()
        self.week_start = self.week_start()
        self.week_end = self.week_end()

    def day_today(self):
        today = date.today()
        return today

    def day_monday(self):
        today = self.day_today
        monday = today - timedelta(days=today.weekday())
        return monday

    def day_tuesday(self):
        monday = self.day_monday
        tuesday = monday + timedelta(days=1)
        return tuesday

    def day_wednesday(self):
        monday = self.day_monday()
        wednesday = monday + timedelta(days=2)
        return wednesday

    def day_thursday(self):
        monday = self.day_monday
        thursday = monday + timedelta(days=3)
        return thursday

    def day_friday(self):
        monday = self.day_monday
        friday = monday + timedelta(days=4)
        return friday

    def day_weekends(self):
        monday = self.day_monday
        saturday = monday + timedelta(days=5)
        sunday = monday + timedelta(days=6)
        return str(saturday.day) + '-' + str(sunday.day)

    def week_start(self):
        today = self.day_today
        monday = today - timedelta(days=today.weekday())
        return monday

    def week_end(self):
        monday = self.day_monday
        week_end = monday + timedelta(days=6)
        return week_end
