from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path(r'', Home, name='Home'),

    path(r'usuario/cadastro', csrf_exempt(Usuario_add.as_view())),
    path(r'usuario/projeto/cadastro', csrf_exempt(Projeto_add.as_view())),
    path(r'usuario/projeto/item/cadastro', csrf_exempt(Item_add.as_view())),
    path(r'usuario/projeto/item/match/cadastro', csrf_exempt(Match_add.as_view())),

    path(r'usuarios', csrf_exempt(Usuarios_list.as_view())),
    path(r'projetos', csrf_exempt(Projetos_list.as_view())),
    path(r'itens', csrf_exempt(Itens_list.as_view())),
    path(r'matchs', csrf_exempt(Matchs_list.as_view())),

    path(r'usuario/projetos', csrf_exempt(UsuarioProjetos_list.as_view())),

    path(r'usuario/projeto/itens', csrf_exempt(UsuarioProjetoItens_list.as_view())),

    path(r'usuario/projeto/item/matchs', csrf_exempt(UsuarioProjetoItemMatchs_list.as_view())),
]
