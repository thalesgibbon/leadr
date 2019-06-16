import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import ExcelWriter




df = pd.DataFrame(columns=['DataAprovacao', 'UF', 'ValorAprovado'])

url = r'http://www2.esporte.gov.br/leiincentivo/leiIncentivoEsporte/consultaProjetosAprovadosAptosCaptacao.do?acao=consultar&dtInicio=01%2F01%2F2018&dtFinal=31%2F12%2F2018&sgUf=&municipioVO.idMunicipio=&nrSLIE=&nmProponente=&nmProjeto=&modalidadeEsportivaVO.idModalidadeEsportiva=0&areaFinalisticaVO.idAreaFinalistica=0&nrProcesso='


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


page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
x = soup.find_all(class_='strong alignRight')
ufs = []
for item in range(1, len(x)):
    ufs.append(x[item].contents[0].contents[0])



ufs.insert(0,'0,00')



df['ValorCaptado'] = ufs



writer = ExcelWriter(r'C:\Users\gustavomartins\Desktop\df1.xlsx')
df.to_excel(writer,'Sheet1', index=False)
writer.save()