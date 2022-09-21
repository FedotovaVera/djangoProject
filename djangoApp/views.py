from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Tasks
from djangoApp import datemanager
from .forms import TasksForm, DeleteForm, UpdateForm
from django.views.generic import DetailView, UpdateView, CreateView


def hello(request):
    dt1 = datemanager.DateManager().day_monday.day
    dt_tsk_1 = datemanager.DateManager().day_monday.strftime("%Y-%m-%d")
    tsk1 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_1)

    dt2 = datemanager.DateManager().day_tuesday.day
    dt_tsk_2 = datemanager.DateManager().day_tuesday.strftime("%Y-%m-%d")
    tsk2 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_2)

    dt3 = datemanager.DateManager().day_wednesday.day
    dt_tsk_3 = datemanager.DateManager().day_wednesday.strftime("%Y-%m-%d")
    tsk3 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_3)

    dt4 = datemanager.DateManager().day_thursday.day
    dt_tsk_4 = datemanager.DateManager().day_thursday.strftime("%Y-%m-%d")
    tsk4 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_4)

    dt5 = datemanager.DateManager().day_friday.day
    dt_tsk_5 = datemanager.DateManager().day_friday.strftime("%Y-%m-%d")
    tsk5 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_5)

    dt6 = datemanager.DateManager().day_saturday.day
    dt_tsk_6 = datemanager.DateManager().day_saturday.strftime("%Y-%m-%d")
    tsk6 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_6)

    dt7 = datemanager.DateManager().day_sunday.day
    dt_tsk_7 = datemanager.DateManager().day_sunday.strftime("%Y-%m-%d")
    tsk7 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_7)

    context = {'day_1': dt1, 'day_2': dt2, 'day_3': dt3, 'day_4': dt4, 'day_5': dt5, 'day_6': dt6, 'day_7': dt7,
               'tsk_1': tsk1, 'tsk_2': tsk2, 'tsk_3': tsk3, 'tsk_4': tsk4, 'tsk_5': tsk5, 'tsk_6': tsk6, 'tsk_7': tsk7}
    return render(request, 'hello.html', context=context)


class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'task-view.html'
    context_object_name = 'task'


class UpdateTask(UpdateView):
    form_class = UpdateForm
    model = Tasks
    template_name = 'update.html'
    success_url = '/'


class DeleteTask(UpdateView):
    form_class = DeleteForm
    model = Tasks
    template_name = 'delete.html'
    success_url = '/'


def AddTask(request):
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            error = 'Форма заполнена неверно'
    form = TasksForm()
    context = {'form': form}
    return render(request, 'addtask.html', context=context)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"