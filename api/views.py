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


def extrai_body(rq):
    request_body = rq.body.decode(encoding='utf-8')
    return dict(parse.parse_qsl(request_body))


""" POST """


class Usuario_add(ListView):

    def post(self, request):
        fields = ['cpf_cnpj', 'senha', 'cnpj_flag', 'nome_completo']
        try:
            request_body = extrai_body(request)

            Usuario.objects.create(
                cpf_cnpj=request_body['cpf_cnpj'],
                senha=request_body['senha'],
                cnpj_flag=request_body['cnpj_flag'],
                nome_completo=request_body['nome_completo']
            )
            result = json.dumps({'status': 'ok'})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


class Conta_add(ListView):

    def post(self, request):
        fields = ['cpf_cnpj', 'banco_id', 'agencia_digito', 'conta_digito', 'poupanca_flag']
        try:
            request_body = extrai_body(request)

            ContaUsuario.objects.create(
                cpf_cnpj=Usuario.objects.get(cpf_cnpj=request_body['cpf_cnpj']),
                banco_id=request_body['banco_id'],
                agencia_digito=request_body['agencia_digito'],
                conta_digito=request_body['conta_digito'],
                poupanca_flag=request_body['poupanca_flag']
            )
            result = json.dumps({'status': 'ok'})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


class Favorecido_add(ListView):

    def post(self, request):
        fields = ['conta_id', 'cpf_cnpj', 'cnpj_flag', 'banco_id', 'agencia_digito', 'conta_digito', 'poupanca_flag']
        try:
            request_body = extrai_body(request)

            Favorecido.objects.create(
                conta_id=ContaUsuario.objects.get(conta_id=request_body['conta_id']),
                cpf_cnpj=request_body['cpf_cnpj'],
                cnpj_flag=request_body['cnpj_flag'],
                banco_id=request_body['banco_id'],
                agencia_digito=request_body['agencia_digito'],
                conta_digito=request_body['conta_digito'],
                poupanca_flag=request_body['poupanca_flag']
            )
            result = json.dumps({'status': 'ok'})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


class Transacao_add(ListView):

    def post(self, request):
        fields = ['conta_id', 'favorecido_id', 'valor_dolar', 'status_id']
        try:
            request_body = extrai_body(request)

            Transacao.objects.create(
                conta_id=ContaUsuario.objects.get(conta_id=request_body['conta_id']),
                favorecido_id=Favorecido.objects.get(favorecido_id=request_body['favorecido_id']),
                valor_dolar=request_body['valor_dolar'],
                status_id=request_body['status_id']
            )
            result = json.dumps({'status': 'ok'})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


class Match_add(ListView):

    def post(self, request):
        fields = ['transacao_id_d2r', 'transacao_id_r2d', 'valor_dolar', 'dolar_conversao']
        try:
            request_body = extrai_body(request)

            Match.objects.create(
                transacao_id_d2r=Transacao.objects.get(transacao_id=request_body['transacao_id_d2r']),
                transacao_id_r2d=Transacao.objects.get(transacao_id=request_body['transacao_id_r2d']),
                valor_dolar=request_body['valor_dolar'],
                dolar_conversao=request_body['dolar_conversao']
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


class Contas_list(ListView):

    def post(self, request):
        records = ContaUsuario.objects.all()  # todos registros
        records = records.values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


class Favorecidos_list(ListView):

    def post(self, request):
        records = Favorecido.objects.all()  # todos registros
        records = records.values()  # filtra os campos
        records = [record for record in records]  # queryset para dict
        records = date_jquery(records, 'data_input', '%F')  # ajusta data
        result = json.dumps({'status': 'ok', 'result': records})
        return HttpResponse(result, content_type='application/json', status=200)


class Transacoes_list(ListView):

    def post(self, request):
        records = Transacao.objects.all()  # todos registros
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


class UsuarioContas_list(ListView):

    def post(self, request):
        fields = ['cpf_cnpj',]
        try:
            request_body = extrai_body(request)
            cpf_cnpj = request_body['cpf_cnpj']

            records = ContaUsuario.objects.all()  # todos registros
            records = records.filter(cpf_cnpj=cpf_cnpj).values()  # filtra os campos
            records = [record for record in records]  # queryset para dict
            records = date_jquery(records, 'data_input', '%F')  # ajusta data
            result = json.dumps({'status': 'ok', 'result': records})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


""" GET TERCEIRO NIVEL """


class UsuarioContaFavorecidos_list(ListView):

    def post(self, request):
        fields = ['conta_id',]
        try:
            request_body = extrai_body(request)
            conta_id = request_body['conta_id']

            records = Favorecido.objects.all()  # todos registros
            records = records.filter(conta_id=conta_id).values()  # filtra os campos
            records = [record for record in records]  # queryset para dict
            records = date_jquery(records, 'data_input', '%F')  # ajusta data
            result = json.dumps({'status': 'ok', 'result': records})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


class UsuarioContaTransacoes_list(ListView):

    def post(self, request):
        fields = ['conta_id',]
        try:
            request_body = extrai_body(request)
            conta_id = request_body['conta_id']

            records = Transacao.objects.all()  # todos registros
            records = records.filter(conta_id=conta_id).values()  # filtra os campos
            records = [record for record in records]  # queryset para dict
            records = date_jquery(records, 'data_input', '%F')  # ajusta data
            result = json.dumps({'status': 'ok', 'result': records})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


""" GET QUARTO NIVEL """


class UsuarioContaTransacaoMatchs_list(ListView):

    def post(self, request):
        fields = ['transacao_id',]
        try:
            request_body = extrai_body(request)
            transacao_id = request_body['transacao_id']

            records = Match.objects.all()  # todos registros
            records = records.filter(Q(transacao_id_d2r=transacao_id) | Q(transacao_id_d2r_id=transacao_id)).values()  # filtra os campos
            records = [record for record in records]  # queryset para dict
            records = date_jquery(records, 'data_input', '%F')  # ajusta data
            result = json.dumps({'status': 'ok', 'result': records})
        except:
            result = json.dumps({'status': f'erro, fields: {fields}'})
        return HttpResponse(result, content_type='application/json', status=200)


