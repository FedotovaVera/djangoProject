from calendar import monthrange
import datetime

current_year = datetime.datetime.now().year
month = datetime.datetime.now().month
days = monthrange(current_year, month)[1]

context = {}
for day in range(1, days+1):
    dt_tsk = datetime.date(day=day, month=month, year=current_year)
    context['day_'+str(day)] = day

print(context)