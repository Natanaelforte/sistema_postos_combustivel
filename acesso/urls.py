from django.urls import path, include
from . import views

app_name = 'acesso'

urlpatterns = [
    path('', views.AcessoLoginView.as_view(), name='login'),
]