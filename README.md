# Envio de Relatórios de Produção por E-mail (PDF)

## Objetivo

Este repositório contém um sistema automatizado para coleta de dados de produção via API, geração de relatórios em PDF e envio por e-mail. A ferramenta foi desenvolvida para facilitar o acompanhamento diário da produção industrial, fornecendo um resumo estruturado das linhas de produção em formato portátil e de fácil acesso.

## Descrição

O script realiza as seguintes etapas:

1. **Coleta de Dados**: Através de requisições HTTP autenticadas, os dados de produção são obtidos diretamente da API.
2. **Processamento**: Os dados de cada linha de produção são organizados e resumidos.
3. **Geração de PDF**: Um relatório em PDF é criado com os dados processados.
4. **Envio por E-mail**: O arquivo PDF é enviado automaticamente para os destinatários configurados.

Este processo é executado diariamente, considerando o intervalo entre a data atual e o dia anterior, com horário inicial fixado em 06:00:00.

## Tecnologias Utilizadas

- Python 3.x
- `requests` – Para comunicação com a API.
- `datetime` – Para manipulação de datas.
- `reportlab` ou biblioteca personalizada (assumida no módulo `pdf.py`) – Para geração de PDF.
- `smtplib` (assumido no módulo `mail.py`) – Para envio de e-mails via protocolo SMTP.

## Estrutura do Projeto

- `main.py` – Script principal de execução.
- `pdf.py` – Responsável por gerar e apagar os arquivos PDF.
- `mail.py` – Responsável por realizar o envio do e-mail com o anexo.
- `apikey.py` – Contém as variáveis `API` e `TOKEN` para autenticação na API de produção.
