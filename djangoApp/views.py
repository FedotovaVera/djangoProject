from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Tasks
from djangoApp import datemanager
from .forms import TasksForm, DeleteForm, UpdateForm, ProfileForm
from django.views.generic import DetailView, UpdateView, CreateView
import datetime
from calendar import monthrange
from .forms import SignUpForm


def hello(request):
    if request.user.is_authenticated:
        user_id = User.objects.all().filter(id=request.user.id)[0].id
    else:
        user_id = 0
    dt1 = datemanager.DateManager().day_monday.day
    dt2 = datemanager.DateManager().day_tuesday.day
    dt3 = datemanager.DateManager().day_wednesday.day
    dt4 = datemanager.DateManager().day_thursday.day
    dt5 = datemanager.DateManager().day_friday.day
    dt6 = datemanager.DateManager().day_saturday.day
    dt7 = datemanager.DateManager().day_sunday.day

    dt_tsk_1 = datemanager.DateManager().day_monday.strftime("%Y-%m-%d")
    dt_tsk_2 = datemanager.DateManager().day_tuesday.strftime("%Y-%m-%d")
    dt_tsk_3 = datemanager.DateManager().day_wednesday.strftime("%Y-%m-%d")
    dt_tsk_4 = datemanager.DateManager().day_thursday.strftime("%Y-%m-%d")
    dt_tsk_5 = datemanager.DateManager().day_friday.strftime("%Y-%m-%d")
    dt_tsk_6 = datemanager.DateManager().day_saturday.strftime("%Y-%m-%d")
    dt_tsk_7 = datemanager.DateManager().day_sunday.strftime("%Y-%m-%d")

    if str(User.objects.get(is_superuser=1)) == str(request.user.username):
        tsk1 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_1)
        tsk2 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_2)
        tsk3 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_3)
        tsk4 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_4)
        tsk5 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_5)
        tsk6 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_6)
        tsk7 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_7)
    else:
        tsk1 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_1, user_id_id=user_id)
        tsk2 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_2, user_id_id=user_id)
        tsk3 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_3, user_id_id=user_id)
        tsk4 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_4, user_id_id=user_id)
        tsk5 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_5, user_id_id=user_id)
        tsk6 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_6, user_id_id=user_id)
        tsk7 = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk_7, user_id_id=user_id)

    context = {'day_1': dt1, 'day_2': dt2, 'day_3': dt3, 'day_4': dt4, 'day_5': dt5, 'day_6': dt6, 'day_7': dt7,
               'tsk_1': tsk1, 'tsk_2': tsk2, 'tsk_3': tsk3, 'tsk_4': tsk4, 'tsk_5': tsk5, 'tsk_6': tsk6, 'tsk_7': tsk7}
    return render(request, 'hello.html', context=context)


def Monthtask(request):
    if request.user.is_authenticated:
        user_id = User.objects.all().filter(id=request.user.id)[0].id
    else:
        user_id = 0
    current_year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    days = monthrange(current_year, month)[1]
    context = {}
    for day in range(1, days + 1):
        dt_tsk = datetime.date(day=day, month=month, year=current_year)
        wkday = datetime.date(day=day, month=month, year=current_year).weekday()
        match wkday:
            case 0:
                dayweek = 'Понедельник'
            case 1:
                dayweek = 'Вторник'
            case 2:
                dayweek = 'Среда'
            case 3:
                dayweek = 'Четверг'
            case 4:
                dayweek = 'Пятница'
            case 5:
                dayweek = 'Суббота'
            case 6:
                dayweek = 'Воскресенье'
        tsk = Tasks.objects.all().order_by('time_task').filter(date_end='', date_task=dt_tsk, user_id_id=user_id)

        context['day_' + str(day)] = day
        context['tsk_' + str(day)] = tsk
        context['dayweek_' + str(day)] = dayweek
    return render(request, 'month.html', context=context)


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
            forma = form.save(commit=False)
            forma.user_id_id = request.user.id
            forma.save()
            return HttpResponseRedirect('/')
        else:
            error = 'Форма заполнена неверно'
    form = TasksForm()
    context = {'form': form}
    return render(request, 'addtask.html', context=context)


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('index-page')
    template_name = 'registration/profile.html'


def ReminderTask(request):
    if request.user.is_authenticated:
        username = User.objects.all().filter(id=request.user.id)[0].username
        first_name = User.objects.all().filter(id=request.user.id)[0].first_name
        last_name = User.objects.all().filter(id=request.user.id)[0].last_name
        context = {'username': username, 'first_name': first_name, 'last_name': last_name}
    return render(request, 'reminder.html', context=context)
