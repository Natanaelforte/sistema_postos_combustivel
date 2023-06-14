from django.urls import path
from . import views

app_name = 'funcao'

urlpatterns = [
    path('', views.FuncaoListView.as_view(), name='list'),
    path('tabela/', views.FuncaoTableView.as_view(), name='table'),
    path('create/', views.FuncaoCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.FuncaoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.FuncaoDeleteView.as_view(), name='delete')
]