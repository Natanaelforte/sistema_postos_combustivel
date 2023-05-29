from django.contrib import admin
from django.urls import path

from posto import views


app_name = 'posto'

urlpatterns = [
    path('', views.posto_json, name='list')
]