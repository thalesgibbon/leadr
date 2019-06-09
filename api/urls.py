"""swapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from .views import *


urlpatterns = [
    path(r'', Home, name='Home'),

    path(r'usuarios', Usuarios_list.as_view()),
    path(r'contas', Contas_list.as_view()),
    path(r'favorecidos', Favorecidos_list.as_view()),
    path(r'transacoes', Transacoes_list.as_view()),
    path(r'matchs', Matchs_list.as_view()),

    path(r'usuario/contas', UsuarioContas_list.as_view()),

    path(r'usuario/conta/transacoes', UsuarioContaTransacoes_list.as_view()),
    path(r'usuario/conta/favorecidos', UsuarioContaFavorecidos_list.as_view()),

    path(r'usuario/conta/transacao/matchs', UsuarioContaTransacaoMatchs_list.as_view()),
]
