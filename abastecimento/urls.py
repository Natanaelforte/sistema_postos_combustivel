from django.urls import path

from abastecimento import views

app_name = 'abastecimento'

urlpatterns = [
    path('', views.AbastecimentoListViewl.as_view(), name='abastecimento_list'),
]
