from django.db import models


class Usuario(models.Model):
    cnpj = models.BigIntegerField(primary_key=True)
    senha = models.CharField(max_length=100)
    empreendedor_flag = models.BooleanField(default=False)
    data_input = models.DateTimeField(auto_now_add=True)


class InfoUsuario(models.Model):
    cnpj = models.BigIntegerField(primary_key=True)
    data_abertura = models.DateField()
    nome_empresarial = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    email = models.CharField(max_length=100)
    data_input = models.DateTimeField(auto_now_add=True)


class Projeto(models.Model):
    projeto_id = models.IntegerField(primary_key=True, auto_created=True)
    cnpj = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    projeto_desc = models.CharField(max_length=100)
    validade_date = models.DateField(auto_now_add=True)
    data_input = models.DateTimeField(auto_now_add=True)


class Item(models.Model):
    item_id = models.IntegerField(primary_key=True, auto_created=True)
    projeto_id = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    item_desc = models.CharField(max_length=100)
    valor = models.FloatField()
    data_input = models.DateTimeField(auto_now_add=True)


class Match(models.Model):
    match_id = models.IntegerField(primary_key=True, auto_created=True)
    cnpj = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    data_input = models.DateTimeField(auto_now_add=True)
