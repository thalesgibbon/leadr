from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status


def Home(request):
    return render(request, 'home.html')


class perfil(APIView):
    def get(self, request):
        pk = request.GET['pk']
        if pk == '1':
            dicio = {
                "nome": "Primo Rico",
                "foto": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Thiago_Nigro_O_Primo_Rico.jpg/800px-Thiago_Nigro_O_Primo_Rico.jpg",
                "patrimonio": "256K",
                "carteira_atual": {
                    "OIBR4": "55K",
                    "TIMP3": "20K",
                    "VIVO4": "25K",
                },
            }
        else:
            dicio = {
                "nome": "Tiago Reis",
                "foto": "https://pbs.twimg.com/profile_images/1057606810432163841/7mBqNTeD_400x400.jpg",
                "patrimonio": "156K",
                "carteira_atual": {
                    "ITUB4": "30K",
                    "BBDC4": "35K",
                    "BBAS3": "35K",
                },
            }
        return Response(data=dicio, status=status.HTTP_200_OK)
