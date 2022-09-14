from django.shortcuts import render
from .models import Profile, Tasks
from djangoApp import datemanager
from django.db.models import Q


def hello(request):
    dt1 = datemanager.DateManager().day_monday.day
    dt_tsk_1 = datemanager.DateManager().day_monday.strftime("%Y-%m-%d")
    tsk1 = Tasks.objects.all().order_by('time_task').filter(date_task=dt_tsk_1)

    dt2 = datemanager.DateManager().day_tuesday.day
    dt_tsk_2 = datemanager.DateManager().day_tuesday.strftime("%Y-%m-%d")
    tsk2 = Tasks.objects.all().order_by('time_task').filter(date_task=dt_tsk_2)

    dt3 = datemanager.DateManager().day_wednesday.day
    dt_tsk_3 = datemanager.DateManager().day_wednesday.strftime("%Y-%m-%d")
    tsk3 = Tasks.objects.all().order_by('time_task').filter(date_task=dt_tsk_3)

    dt4 = datemanager.DateManager().day_thursday.day
    dt_tsk_4 = datemanager.DateManager().day_thursday.strftime("%Y-%m-%d")
    tsk4 = Tasks.objects.all().order_by('time_task').filter(date_task=dt_tsk_4)

    dt5 = datemanager.DateManager().day_friday.day
    dt_tsk_5 = datemanager.DateManager().day_friday.strftime("%Y-%m-%d")
    tsk5 = Tasks.objects.all().order_by('time_task').filter(date_task=dt_tsk_5)

    dt6 = datemanager.DateManager().day_weekends
    dt_tsk_6 = datemanager.DateManager().day_saturday.strftime("%Y-%m-%d")
    dt_tsk_7 = datemanager.DateManager().day_sunday.strftime("%Y-%m-%d")
    tsk6 = Tasks.objects.all().order_by('time_task').filter(date_task=dt_tsk_6)
    tsk7 = Tasks.objects.all().order_by('time_task').filter(date_task=dt_tsk_7)

    context = {'day_1': dt1, 'day_2': dt2, 'day_3': dt3, 'day_4': dt4, 'day_5': dt5, 'day_6': dt6,
               'tsk_1': tsk1, 'tsk_2': tsk2, 'tsk_3': tsk3, 'tsk_4': tsk4, 'tsk_5': tsk5, 'tsk_6': tsk6, 'tsk_7': tsk7}
    return render(request, 'hello.html', context=context)

    """
#вытащить из таблицы
def main(request): #вытащить из таблицы
    context = {'fromdb': Maine.objects.all()[0].position}
    return render(request, 'main.html', context=context)


    #занести в таблицу
    ex = Maine()
    ex.user = '100pir'
    ex.position = 'something'
    ex.birth_date = '15-06-1991'
    ex.save()
    return render(request, 'main.html')
"""
