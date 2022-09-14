from django.shortcuts import render
from .models import Profile, Tasks
from djangoApp import datemanager
from django.db.models import Q


def hello(request):
    dt1 = datemanager.DateManager().day_monday.day
    dt_tsk_1 = datemanager.DateManager().day_monday.strftime("%Y-%m-%d")
    tsk1 = ''
    if Tasks.objects.all().filter(date_task=dt_tsk_1).count() != 0:
        for i in range(Tasks.objects.all().filter(date_task=dt_tsk_1).count()):
            tsk1 += Tasks.objects.all().filter(date_task=dt_tsk_1)[i].task_name + '\n'
    else:
        tsk1 = 'На этот день не установлено задач'

    dt2 = datemanager.DateManager().day_tuesday.day
    dt_tsk_2 = datemanager.DateManager().day_tuesday.strftime("%Y-%m-%d")
    tsk2 = ''
    if Tasks.objects.all().filter(date_task=dt_tsk_2).count() != 0:
        for i in range(Tasks.objects.all().filter(date_task=dt_tsk_2).count()):
            tsk2 += Tasks.objects.all().filter(date_task=dt_tsk_2)[i].task_name + '\n'
    else:
        tsk2 = 'На этот день не установлено задач'

    dt3 = datemanager.DateManager().day_wednesday.day
    dt_tsk_3 = datemanager.DateManager().day_wednesday.strftime("%Y-%m-%d")
    tsk3 = ''
    if Tasks.objects.all().filter(date_task=dt_tsk_3).count() != 0:
        for i in range(Tasks.objects.all().filter(date_task=dt_tsk_3).count()):
            tsk3 += Tasks.objects.all().filter(date_task=dt_tsk_3)[i].task_name + '\n'
    else:
        tsk3 = 'На этот день не установлено задач'

    dt4 = datemanager.DateManager().day_thursday.day
    dt_tsk_4 = datemanager.DateManager().day_thursday.strftime("%Y-%m-%d")
    tsk4 = ''
    if Tasks.objects.all().filter(date_task=dt_tsk_4).count() != 0:
        for i in range(Tasks.objects.all().filter(date_task=dt_tsk_4).count()):
            tsk4 += Tasks.objects.all().filter(date_task=dt_tsk_4)[i].task_name + '\n'
    else:
        tsk4 = 'На этот день не установлено задач'

    dt5 = datemanager.DateManager().day_friday.day
    dt_tsk_5 = datemanager.DateManager().day_friday.strftime("%Y-%m-%d")
    tsk5 = ''
    if Tasks.objects.all().filter(date_task=dt_tsk_5).count() != 0:
        for i in range(Tasks.objects.all().filter(date_task=dt_tsk_5).count()):
            tsk5 += Tasks.objects.all().filter(date_task=dt_tsk_5)[i].task_name + '\n'
    else:
        tsk5 = 'На этот день не установлено задач'

    dt6 = datemanager.DateManager().day_weekends
    dt_tsk_6 = datemanager.DateManager().day_saturday.strftime("%Y-%m-%d")
    dt_tsk_7 = datemanager.DateManager().day_sunday.strftime("%Y-%m-%d")
    tsk6 = ''
    if Tasks.objects.all().filter(Q(date_task=dt_tsk_6) | Q(date_task=dt_tsk_7)).count() != 0:
        for i in range(Tasks.objects.all().filter(Q(date_task=dt_tsk_6) | Q(date_task=dt_tsk_7)).count()):
            tsk6 += Tasks.objects.all().filter(Q(date_task=dt_tsk_6) | Q(date_task=dt_tsk_7))[i].task_name + '\n'
    else:
        tsk6 = 'На выходные не установлено заметок'

    context = {'day_1': dt1, 'day_2': dt2, 'day_3': dt3, 'day_4': dt4, 'day_5': dt5, 'day_6': dt6,
               'tsk_1': tsk1, 'tsk_2': tsk2, 'tsk_3': tsk3, 'tsk_4': tsk4, 'tsk_5': tsk5, 'tsk_6': tsk6}
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
