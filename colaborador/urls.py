from django.contrib import admin
from django.urls import path

from colaborador import views

app_name = 'colaborador'

urlpatterns = [
    path('', views.ColaboradorListViewl.as_view(), name='colaborador_list')
]