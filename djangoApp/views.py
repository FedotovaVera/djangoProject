from django.shortcuts import render
from djangoApp import datemanager
from djangoApp import showtask


def hello(request):
    context = {'day_1': str(datemanager.day_monday().day), 'day_2': str(datemanager.day_tuesday().day),
               'day_3': str(datemanager.day_wednesday().day), 'day_4': str(datemanager.day_thursday().day),
               'day_5': str(datemanager.day_friday().day), 'day_6': str(datemanager.day_weekends()),
               'date_task': str(showtask.date_task()), 'time_task': str(showtask.time_task()),
               'task_name': str(showtask.task_name())}
    return render(request, 'hello.html', context)


