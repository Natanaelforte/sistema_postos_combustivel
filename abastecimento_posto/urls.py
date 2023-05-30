"""
URL configuration for abastecimento_posto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('acesso/', include('acesso.urls')),
    path('inicio/', include('inicio.urls')),
    path('posto/', include('posto.urls')),
    path('lista_colaboradores/', include('colaborador.urls')),
    path('lista_bombas/', include('bomba_de_combustivel.urls')),
    path('lista_combustivel/', include('combustivel.urls')),
    path('lista_funcao/', include('funcao.urls')),
    path('lista_tanque/', include('tanque.urls')),
    path('lista_abastecimento/', include('abastecimento.urls'))
]
