from django.views.generic import ListView
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core import serializers
import json
from urllib import parse
from django.db.models import Q


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


""" PRIMEIRO NIVEL """


class Usuarios_list(ListView):

    def get(self, request):
        records = Usuario.objects.all()  # todos registros
        records = records.values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


class Contas_list(ListView):

    def get(self, request):
        records = ContaUsuario.objects.all()  # todos registros
        records = records.values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


class Favorecidos_list(ListView):

    def get(self, request):
        records = Favorecido.objects.all()  # todos registros
        records = records.values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


class Transacoes_list(ListView):

    def get(self, request):
        records = Transacao.objects.all()  # todos registros
        records = records.values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


class Matchs_list(ListView):

    def get(self, request):
        records = Match.objects.all()  # todos registros
        records = records.values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


""" SEGUNDO NIVEL """


class UsuarioContas_list(ListView):

    def get(self, request):
        request_body = request.body.decode(encoding='utf-8')
        request_body = dict(parse.parse_qsl(request_body))
        cpf_cnpj = request_body['cpf_cnpj']

        records = ContaUsuario.objects.all()  # todos registros
        records = records.filter(cpf_cnpj=cpf_cnpj).values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


""" TERCEIRO NIVEL """


class UsuarioContaFavorecidos_list(ListView):

    def get(self, request):
        request_body = request.body.decode(encoding='utf-8')
        request_body = dict(parse.parse_qsl(request_body))
        conta_id = request_body['conta_id']

        records = Favorecido.objects.all()  # todos registros
        records = records.filter(conta_id=conta_id).values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


class UsuarioContaTransacoes_list(ListView):

    def get(self, request):
        request_body = request.body.decode(encoding='utf-8')
        request_body = dict(parse.parse_qsl(request_body))
        conta_id = request_body['conta_id']

        records = Transacao.objects.all()  # todos registros
        records = records.filter(conta_id=conta_id).values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


""" QUARTO NIVEL """


class UsuarioContaTransacaoMatchs_list(ListView):

    def get(self, request):
        request_body = request.body.decode(encoding='utf-8')
        request_body = dict(parse.parse_qsl(request_body))
        transacao_id = request_body['transacao_id']

        records = Match.objects.all()  # todos registros
        records = records.filter(Q(transacao_id_d2r=transacao_id) | Q(transacao_id_d2r_id=transacao_id)).values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


