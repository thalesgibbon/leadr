from django.views.generic import ListView
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core import serializers
import json
from urllib import parse


""" CONFIG """


def date_jquery(qs, key_name, date_format='%Y-%M-%d'):
    import datetime
    data = {}
    for k, registro in enumerate(qs):
        registro.update({key_name: registro[key_name].strftime(date_format)})
        data[k] = registro
    return data


def to_json(objects, values=None):
    if values:
        if type(values) == tuple:
            return serializers.serialize('json', objects, fields=values)
        else:
            raise Exception('inserir uma tupla no parametro values')
    else:
        return serializers.serialize('json', objects)


def Home(request):
    return render(request, 'home.html')


def extrai_body(rq):
    request_body = rq.body.decode(encoding='utf-8')
    return dict(parse.parse_qsl(request_body))


""" POST """


class Usuario_add(ListView):

    def post(self, request):
        fields = ['cnpj', 'senha', 'empreendedor_flag']
        try:
            request_body = extrai_body(request)

            Usuario.objects.create(
                cnpj=request_body['cnpj'],
                senha=request_body['senha'],
                empreendedor_flag=request_body['empreendedor_flag']
            )
            result = json.dumps({'status': 'ok'})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


class Projeto_add(ListView):

    def post(self, request):
        fields = ['cnpj', 'projeto_desc', 'validade_date']
        try:
            request_body = extrai_body(request)

            Projeto.objects.create(
                cnpj=Usuario.objects.get(cnpj=request_body['cnpj']),
                projeto_desc=request_body['projeto_desc'],
                validade_date=request_body['validade_date']
            )
            result = json.dumps({'status': 'ok'})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


class Item_add(ListView):

    def post(self, request):
        fields = ['projeto_id', 'item_desc', 'valor']
        try:
            request_body = extrai_body(request)

            Item.objects.create(
                projeto_id=Projeto.objects.get(projeto_id=request_body['projeto_id']),
                item_desc=request_body['item_desc'],
                valor=request_body['valor_dolar']
            )
            result = json.dumps({'status': 'ok'})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


class Match_add(ListView):

    def post(self, request):
        fields = ['cnpj', 'item_id']
        try:
            request_body = extrai_body(request)

            Match.objects.create(
                cnpj=Usuario.objects.get(cnpj=request_body['cnpj']),
                item_id=Item.objects.get(item_id=request_body['item_id'])
            )
            result = json.dumps({'status': 'ok'})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


""" GET PRIMEIRO NIVEL """


class Usuarios_list(ListView):

    def post(self, request):
        records = Usuario.objects.all()  # todos registros
        records = records.values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


class Projetos_list(ListView):

    def post(self, request):
        records = Projeto.objects.all()  # todos registros
        records = records.values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


class Itens_list(ListView):

    def post(self, request):
        records = Item.objects.all()  # todos registros
        records = records.values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


class Matchs_list(ListView):

    def post(self, request):
        records = Match.objects.all()  # todos registros
        records = records.values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


""" GET SEGUNDO NIVEL """


class UsuarioProjetos_list(ListView):

    def post(self, request):
        fields = ['cnpj',]
        try:
            request_body = extrai_body(request)
            cnpj = request_body['cnpj']

            records = Projeto.objects.all()  # todos registros
            records = records.filter(cnpj=cnpj).values()  # filtra os campos
            records = [record for record in records]  # queryset para dict
            records = date_jquery(records, 'data_input', '%F')  # ajusta data
            result = json.dumps({'status': 'ok', 'result': records})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


""" GET TERCEIRO NIVEL """


class UsuarioProjetoItens_list(ListView):

    def post(self, request):
        fields = ['projeto_id',]
        try:
            request_body = extrai_body(request)
            projeto_id = request_body['projeto_id']

            records = Item.objects.all()  # todos registros
            records = records.filter(projeto_id=projeto_id).values()  # filtra os campos
            records = [record for record in records]  # queryset para dict
            records = date_jquery(records, 'data_input', '%F')  # ajusta data
            result = json.dumps({'status': 'ok', 'result': records})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


""" GET QUARTO NIVEL """


class UsuarioProjetoItemMatchs_list(ListView):

    def post(self, request):
        fields = ['item_id',]
        try:
            request_body = extrai_body(request)
            item_id = request_body['item_id']

            records = Match.objects.all()  # todos registros
            records = records.filter(item_id=item_id).values()  # filtra os campos
            records = [record for record in records]  # queryset para dict
            records = date_jquery(records, 'data_input', '%F')  # ajusta data
            result = json.dumps({'status': 'ok', 'result': records})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


