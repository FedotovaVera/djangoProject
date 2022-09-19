from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse
from django.urls import reverse

"""
class Maine(models.Model):
    user = models.TextField(max_length=500, blank=True)
    position = models.TextField(max_length=500, blank=True)
    birth_date = models.TextField(max_length=500, blank=True)
"""

class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.TextField(max_length=500, blank=True)
    position = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Tasks(models.Model):
    """
    Таблица, где хранятся актуальные задачи и история
    """
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
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


"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""