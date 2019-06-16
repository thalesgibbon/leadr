import requests
# from bs4 import BeautifulSoup
import pandas as pd
from urllib import parse


url = r'http://www2.esporte.gov.br/leiincentivo/leiIncentivoEsporte/consultaProjetosAprovadosAptosCaptacao.do'

parametros = {}
parametros['acao'] = 'consultar'
parametros['dtInicio'] = '01-01-2018'
parametros['dtFinal'] = '31-12-2018'
parametros['sgUf'] = ''
parametros['municipioVO.idMunicipio'] = ''
parametros['nrSLIE'] = ''
parametros['nmProponente'] = ''
parametros['nmProjeto'] = ''
parametros['modalidadeEsportivaVO.idModalidadeEsportiva'] = '0'
parametros['areaFinalisticaVO.idAreaFinalistica'] = '0'
parametros['nrProcesso'] = ''

r = requests.get(url=url, params=parametros)
r_content = r.content
def extrai_body(rq):
    request_body = rq.body.decode(encoding='utf-8')
    return dict(parse.parse_qsl(request_body))

r.json()

# In[4]:


#url=r'http://www2.esporte.gov.br/leiincentivo/leiIncentivoEsporte/consultaProjetosAprovadosAptosCaptacao.do?acao=consultar&dtInicio=01%2F01%2F2019&dtFinal=30%2F01%2F2019&sgUf=&municipioVO.idMunicipio=&nrSLIE=&nmProponente=&nmProjeto=&modalidadeEsportivaVO.idModalidadeEsportiva=0&areaFinalisticaVO.idAreaFinalistica=0&nrProcesso='
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
x = soup.find_all('table', class_='tabelaConteudo')
ufs = []
for item in range(1, len(x)):
    uf = x[item].select('td b')[5]
    uf = uf.contents[0]
    data_aprovacao = x[item].select('td b')[15]
    data_aprovacao = data_aprovacao.contents[0]
    valor_aprovado = x[item].select('td b')[11]
    valor_aprovado = valor_aprovado.contents[0]
    df = df.append({'UF': uf, 'DataAprovacao': data_aprovacao, 'ValorAprovado' : valor_aprovado}, ignore_index=True)


# In[5]:


df