from django.contrib import admin
from django.urls import path

from colaborador import views

app_name = 'colaborador'

urlpatterns = [
    path('', views.ColaboradorListViewl.as_view(), name='colaborador_list'),
    path('create/', views.ColaboradorCreate.as_view(), name='create'),
]