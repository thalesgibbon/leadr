from django.db import models


class Usuario(models.Model):
    cpf_cnpj = models.BigIntegerField(primary_key=True)
    senha = models.CharField(max_length=100)
    cnpj_flag = models.BooleanField(default=False)
    nome_completo = models.CharField(max_length=100)
    data_input = models.DateTimeField(auto_now_add=True)


class ContaUsuario(models.Model):
    conta_id = models.IntegerField(primary_key=True, auto_created=True)
    cpf_cnpj = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    banco_id = models.IntegerField()
    agencia_digito = models.IntegerField()
    conta_digito = models.IntegerField()
    poupanca_flag = models.BooleanField(default=False)
    data_input = models.DateTimeField(auto_now_add=True)


class Favorecido(models.Model):
    favorecido_id = models.IntegerField(primary_key=True, auto_created=True)
    conta_id = models.ForeignKey(ContaUsuario, on_delete=models.CASCADE)
    cpf_cnpj = models.BigIntegerField()
    cnpj_flag = models.BooleanField(default=False)
    banco_id = models.IntegerField()
    agencia_digito = models.IntegerField()
    conta_digito = models.IntegerField()
    poupanca_flag = models.BooleanField(default=False)
    data_input = models.DateTimeField(auto_now_add=True)


class Transacao(models.Model):
    transacao_id = models.IntegerField(primary_key=True, auto_created=True)
    conta_id = models.ForeignKey(ContaUsuario, on_delete=models.CASCADE)
    favorecido_id = models.ForeignKey(Favorecido, on_delete=models.CASCADE)
    valor_dolar = models.FloatField()
    status_id = models.IntegerField()
    data_input = models.DateTimeField(auto_now_add=True)


class Match(models.Model):
    match_id = models.IntegerField(primary_key=True, auto_created=True)
    transacao_id_d2r = models.ForeignKey(Transacao, on_delete=models.CASCADE, related_name='dolar')
    transacao_id_r2d = models.ForeignKey(Transacao, on_delete=models.CASCADE, related_name='real')
    valor_dolar = models.FloatField()
    dolar_conversao = models.FloatField()
    data_input = models.DateTimeField(auto_now_add=True)