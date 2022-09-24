from djangoApp import views
"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addtask/', views.AddTask, name='add-task'),
    path('<int:pk>/view', views.TaskDetailView.as_view(), name='view-task'),
    path('<int:pk>/update', views.UpdateTask.as_view(), name='update-task'),
    path('<int:pk>/delete', views.DeleteTask.as_view(), name='delete-task'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('month/', views.Monthtask, name='month'),
    path('', views.hello, name='index-page')
]
