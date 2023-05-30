from django.urls import path
from . import views

app_name = 'funcao'

urlpatterns = [
    path('', views.FuncaoListViewl.as_view(), name='funcao_list'),
    path('create/', views.FuncaoCreate.as_view(), name='create')
]