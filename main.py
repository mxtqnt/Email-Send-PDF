import requests
from datetime import datetime, timedelta
from pdf import gerar_pdf, delete_files
from mail import enviar
from apikey import API, TOKEN

delete_files('anexos')

hoje = str(datetime.now())[0:10] + 'T06:00:00'
ontem = str(datetime.now() - timedelta(1))[0:10] + 'T06:00:00'

headers = {
'Authorization': f'token {TOKEN}'
}   

# Pegar linhas
linhas = requests.get((API + 'line/'), headers=headers)

linhas = linhas.json()
dados = []

for item in linhas:
    params = {
        'date_from': ontem,
        'date_to': hoje,
        'line': item['id']
    }
    
    r = requests.get((API + 'production_sheet/'), params=params, headers=headers)

    data = r.json()
    total_sv = data['total_sv']
    total_esteira = data['total_esteira']
    diff_sv = data['diff_sv']

    linha_producao = {
        "nome"      : str(item['name']),
        "sv"        : total_sv,
        "esteira"   : total_esteira,
        "diferenca" : diff_sv
    }

    dados.append(linha_producao)
    
gerar_pdf(dados)
enviar()