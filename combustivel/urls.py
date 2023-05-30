from django.contrib import admin
from django.urls import path

from combustivel import views

app_name = 'combustivel'

urlpatterns = [
    path('', views.CombustivelListViewl.as_view(), name='combustivel_list'),
]