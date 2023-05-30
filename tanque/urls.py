from django.contrib import admin
from django.urls import path

from tanque import views

app_name = 'tanque'

urlpatterns = [
    path('', views.TanqueListViewl.as_view(), name='tanque_list'),
]