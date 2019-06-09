## Projeto
Projeto com objetivo de conhecer a populacao bancarizada que nao utilizam o banco para transferencias internacionais por motivos de reducao de custo. A plataforma faz a intermediacao dessas transferencias, identificam transferencias semelhantes e para consiliar de forma simultanea um swap internacional.

##### Link:
API: https://github.com/thalesgibbon/swapp

Mobile: https://github.com/joaoscheuermann/swapp

PPT Pitch: https://docs.google.com/presentation/d/1eFpw7t9NkY431srxoMS4ZMUWpQ9kZ-I4M75VDhdbG8w/edit#slide=id.p

PPT Full: https://docs.google.com/presentation/d/1OyB2Nyyq0lMSc2g91Ta1TgxzaG9B1VbaNRlHOgDe08g/edit?usp=sharing

| Nome | GitHub 
|---|---|
| Thales Gibbon | @thalesgibbon |
| Joao Scheuermann  | @joaoscheuermann  |
| Adirson Allen |  @ |
| Athena Amar | @ |

## CODE - passo a passo realizado

##### 1. Passos para criacao do zero
```
pip install django 
django-admin startproject swapp .
python manage.py startapp api
python manage.py runserver
```
##### 2. Criacao de models

##### 3. Atualizando banco de dados
```
python manage.py makemigrations
python manage.py migrate
```
##### 4. Input de dados iniciais
```python
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
```

##### 5. deletar registros
```python
Usuario.objects.filter(id=1).delete()
```

##### 6. criando o requirement
```
pip freeze > requirements.txt
```

##### 7. Ajuste do Allow Host
```python
ALLOWED_HOSTS = ['*']
```

##### 8. Abrir a posta 80
* No menu Iniciar , clique em Painel de Controle, em Sistema e Segurançae, em seguida, em Firewall do Windows. O Painel de controle não está configurado para a exibição 'Categoria', você precisa selecionar apenas a opção Firewall do Windows.
* Clique em Configurações Avançadas.
* Clique em Regras de entrada.
* Clique em Nova Regra na janela Ações.
* Clique em Tipo de Regra de porta.
* Clique em Avançar.
* Na página Protocolos e Portas , clique em TCP.
* Selecione Portas Locais Específicas e digite um valor de 80.
* Clique em Avançar.
* Na página Ação , clique em Permitir a conexão.
* Clique em Avançar.
* Na página Perfil , clique nas opções adequadas para seu ambiente.
* Clique em Avançar.
* Na página Nome , digite o nome doReportServer (TCP na porta 80)
* Clique em Concluir.
* Reinicie o computador.

##### 9. baixando as libs necessarias do clone
```
pip install -r requirements.txt
```

##### 10. acessos
* ip aws: ec2-18-207-210-129.compute-1.amazonaws.com
* usuario: Administrator
* senha: 4(LZ-Ee.!ZCVjTEmCytOt-@hImlodUpS
* ip publico: 18.207.210.129
* acesso home: http://ec2-18-207-210-129.compute-1.amazonaws.com/

##### 11. comando de start
python ./manage.py runserver ec2-18-207-210-129.compute-1.amazonaws.com:80