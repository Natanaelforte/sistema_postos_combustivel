from django.contrib import admin
from django.urls import path

from colaborador import views

app_name = 'colaborador'

urlpatterns = [
    path('', views.ColaboradorListView.as_view(), name='list'),
    path('create/', views.ColaboradorCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ColaboradorUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ColaboradorDeleteView.as_view(), name='delete')
]