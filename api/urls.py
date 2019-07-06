from .views import *
from django.conf.urls import url


urlpatterns = [
    url(r'^perfil', perfil.as_view(), name='perfil'),
]
