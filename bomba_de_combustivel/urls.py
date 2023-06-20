from django.urls import path

from bomba_de_combustivel import views

app_name = 'bomba_de_combustivel'

urlpatterns = [
    path('', views.BombaListView.as_view(), name='list'),
    path('tabela/', views.BombaTableView.as_view(), name='table'),
    path('select/', views.BombaSelectView.as_view(), name='select'),
    path('criar/', views.BombaCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.BombaUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.BombaDeleteView.as_view(), name='delete')
]