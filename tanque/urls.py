from django.urls import path

from tanque import views

app_name = 'tanque'

urlpatterns = [
    path('', views.TanqueListView.as_view(), name='list'),
    path('tabela/', views.TanqueTableView.as_view(), name='table'),
    path('create/', views.TanqueCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.TanqueUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TanqueDeleteView.as_view(), name='delete'),
    path('precounitario/', views.PrecoUnitario.as_view(), name='preco-unitario'),
]