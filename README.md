## PROJETO INCENTIVA
Objetivo do projeto eh melhorar a saude publica atraves do esporte, alavancado pela lei do incentivo ao esporte.

Como nossa persona, temos um integrante no grupo que por um bom tempo foi gestor de um clube esportivo. Por muito tempo tentou recolher patrocinio atraves da lei do incentivo, porem desistiu devido a alta burocracia.

Nossa solucao facilita a criacao de projetos, solicitando apenas informacoes extremamente necessarias. Como futuros objetivos, pretendemos fazer integracao via api com sistemas do governo para reduzir a quantidade de documentos a serem confeccionados. Tambem vamos dar visibilidade as empresas e projetos para que se conectem e utilizem mais o incentivo.



### links:

BACKEND: https://github.com/thalesgibbon/incentiva.git

PROTOTIPO: https://www.figma.com/proto/ID1cWEbQi2EDmvnm1E2dLAxl/Untitled?node-id=1%3A3&scaling=min-zoom


PPT: https://www.figma.com/proto/ID1cWEbQi2EDmvnm1E2dLAxl/Untitled?node-id=5%3A10&scaling=contain

REFERENCIAS - lei de incentivo ao esporte: http://www.planalto.gov.br/ccivil_03/_Ato2004-2006/2006/Lei/L11438.htm
 
REFERENCIAS - ministerio do esporte: http://www.esporte.gov.br

REFERENCIA - estatistica: http://www.brasil2016.gov.br/pt-br/incentivo-ao-esporte/lei-de-incentivo-ao-esporte


### Equipe MaisEsportes
| Nome | GitHub 
|---|---|
| Gustavo Borges |  @gustavoro |
| Joao Scheuermann  | @joaoscheuermann  |
| Marcus Vinicius | @ |
| Reginaldo Kono | @regikono |
| Thales Gibbon | @thalesgibbon |

### Inputs iniciais
```
python manage.py shell
from api.models import *

Usuario.objects.create(cnpj = 28172787000198, senha = 'urra', empreendedor_flag = False)
Projeto.objects.create(cnpj = Usuario.objects.get(cnpj=28172787000198), projeto_desc = 'FA nas Escolas', validade_date = '2019-01-01 00:00:00.000')
Item.objects.create(projeto_id=Projeto.objects.get(projeto_id=1), item_desc='bolas infantil', valor=10.00)
Match.objects.create(cnpj = Usuario.objects.get(cnpj=28172787000198), item_id = Item.objects.get(item_id=21))

U = Usuario.objects.filter(cnpj = 28172787000198)
U.delete()

post >> http://127.0.0.1:8000/usuario/cadastro
body >> cnpj = 28172787000198

tabela = Usuario.objects.all().values()
for registro in tabela: print(registro);

tabela = InfoUsuario.objects.all().values()
for registro in tabela: print(registro);

exit()
```