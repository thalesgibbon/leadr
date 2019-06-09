# setup
pip install django 
django-admin startproject swapp .
python manage.py startapp api
python manage.py runserver

# cria registro
python manage.py shell
from api.models import *

Usuario.objects.create(cpf_cnpj = 42862386871, senha = 'popozao', cnpj_flag = False, nome_completo = 'Joao Scheuermann')
ContaUsuario.objects.create(cpf_cnpj = Usuario.objects.get(cpf_cnpj=42862386871), banco_id = 6, agencia_digito = 1234, conta_digito = 567890)
Favorecido.objects.create(conta_id=ContaUsuario.objects.get(cpf_cnpj=42862386871), cpf_cnpj=5252525252, banco_id=1, agencia_digito=5252, conta_digito=525252, cnpj_flag=False)
Transacao.objects.create(conta_id = ContaUsuario.objects.get(conta_id=3), favorecido_id = Favorecido.objects.get(favorecido_id=2), valor_dolar = 25., status_id = 1)
Match.objects.create(transacao_id_d2r = Transacao.objects.get(transacao_id=1), transacao_id_r2d = Transacao.objects.get(transacao_id=2), valor_dolar = 25., dolar_conversao = 4.)

tabela = Match.objects.all().values()
for registro in tabela:
    print(registro)
exit()

x.delete()

#
porta 80
allow host django

ec2-18-207-210-129.compute-1.amazonaws.com
Administrator
4(LZ-Ee.!ZCVjTEmCytOt-@hImlodUpS
18.207.210.129
http://ec2-18-207-210-129.compute-1.amazonaws.com/