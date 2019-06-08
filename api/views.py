from django.views.generic import ListView
from django.shortcuts import render


def Home(request):
    return render(request, 'home.html')