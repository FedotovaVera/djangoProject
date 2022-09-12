from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)


class Tasks(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    task_name = models.CharField(max_length=250)
    task_comment = models.CharField(max_length=4000)
    date_add = models.CharField(max_length=250)
    date_end = models.CharField(max_length=250)
    date_task = models.CharField(max_length=250)
    time_task = models.CharField(max_length=250)
