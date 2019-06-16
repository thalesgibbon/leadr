import requests
import json


class GetCnpj(object):
    def __init__(self, cnpj):
        self.cnpj = str(cnpj)
        self.key = 'Bearer 9be74fc9dfe2cf0f86c399b5cfbfa320'
        self.url = f'https://apigateway.serpro.gov.br/consulta-cnpj-df/v1/cnpj/{self.cnpj}'

    def reload(self, ):
        info = requests.get(self.url, headers={'Authorization': self.key})
        dicio = {}
        if info.status_code == 200:
            info = json.loads(info.content.decode('utf-8'))
            dicio['cnpj'] = info['ni']
            dicio['data_abertura'] = info['data_abertura']
            dicio['nome_empresarial'] = info['nome_empresarial']
            dicio['nome_fantasia'] = info['nome_fantasia']
            dicio['uf'] = info['endereco']['uf']
            dicio['email'] = info['correio_eletronico']
            return dicio
        else:
            return dicio
