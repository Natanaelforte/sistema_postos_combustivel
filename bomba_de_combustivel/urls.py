from django.contrib import admin
from django.urls import path

from bomba_de_combustivel import views

app_name = 'bomba_de_combustivel'

urlpatterns = [
    path('', views.BombaListViewl.as_view(), name='bomba'),
    path('criar/', views.BombaCreate.as_view(), name='create')
]