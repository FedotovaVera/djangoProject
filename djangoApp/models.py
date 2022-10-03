from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Tasks(models.Model):
    """
    Таблица, где хранятся актуальные задачи и история
    """
    id = models.IntegerField(primary_key=True, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_name = models.CharField(max_length=250)
    task_comment = models.CharField(max_length=4000)
    date_add = models.CharField(max_length=250)
    date_end = models.CharField(max_length=250)
    date_task = models.CharField(max_length=250)
    time_task = models.CharField(max_length=250)

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('index-page')

