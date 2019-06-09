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
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path(r'', Home, name='Home'),

    path(r'usuario/cadastro', csrf_exempt(Usuario_add.as_view())),
    path(r'usuario/conta/cadastro', csrf_exempt(Conta_add.as_view())),
    path(r'usuario/conta/favorecido/cadastro', csrf_exempt(Favorecido_add.as_view())),
    path(r'usuario/conta/transacao/cadastro', csrf_exempt(Transacao_add.as_view())),
    path(r'usuario/conta/transacao/match/cadastro', csrf_exempt(Match_add.as_view())),

    path(r'usuarios', csrf_exempt(Usuarios_list.as_view())),
    path(r'contas', csrf_exempt(Contas_list.as_view())),
    path(r'favorecidos', csrf_exempt(Favorecidos_list.as_view())),
    path(r'transacoes', csrf_exempt(Transacoes_list.as_view())),
    path(r'matchs', csrf_exempt(Matchs_list.as_view())),

    path(r'usuario/contas', csrf_exempt(UsuarioContas_list.as_view())),

    path(r'usuario/conta/transacoes', csrf_exempt(UsuarioContaTransacoes_list.as_view())),
    path(r'usuario/conta/favorecidos', csrf_exempt(UsuarioContaFavorecidos_list.as_view())),

    path(r'usuario/conta/transacao/matchs', csrf_exempt(UsuarioContaTransacaoMatchs_list.as_view())),
]
