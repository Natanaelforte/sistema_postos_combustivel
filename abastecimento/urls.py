from django.urls import path

from abastecimento import views

app_name = 'abastecimento'

urlpatterns = [
    path('', views.AbastecimentoListView.as_view(), name='list'),
    path('relatorio/', views.AbastecimentoRelatorioPdf.as_view(), name='relatorio'),
    path('tabela/', views.AbastecimentoTableView.as_view(), name='table'),
    path('valor/', views.AbastecimentoValorTotal.as_view(), name='valor'),
    path('create/', views.AbastecimentoAbastecerView.as_view(), name='create'),
    path('update/<int:pk>/', views.AbastecimentoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.AbastecimentoDeleteView.as_view(), name='delete')
]
