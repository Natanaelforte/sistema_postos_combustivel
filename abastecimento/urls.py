from django.urls import path

from abastecimento import views

app_name = 'abastecimento'

urlpatterns = [
    path('', views.AbastecimentoListView.as_view(), name='list'),
    path('create/', views.AbastecimentoCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.AbastecimentoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.AbastecimentoDeleteView.as_view(), name='delete')
]
