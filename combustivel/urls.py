from django.contrib import admin
from django.urls import path

from combustivel import views

app_name = 'combustivel'

urlpatterns = [
    path('', views.CombustivelListView.as_view(), name='list'),
    path('tabela/', views.CombustivelTableView.as_view(), name='table'),
    path('create/', views.CombustivelCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.CombustivelUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CombustivelDeleteView.as_view(), name='delete')
]