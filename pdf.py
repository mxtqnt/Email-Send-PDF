from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def delete_files(path):
   try:
     files = os.listdir(path)
     for file in files:
       file_path = os.path.join(path, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
   except OSError:
     print("Erro.")

def gerar_pdf(data):
    x_linha = 700

    c = canvas.Canvas(('anexos/relatorio_' + str(datetime.now())[0:10] + '.pdf'), pagesize=A4)
    c.setTitle("Relatório de Produção")
    c.drawString(100, 750, "Relatório de Produção dia " + str(datetime.now())[0:10])

    for linha in data:
        # Cabeçalho
        c.drawString(100, x_linha, linha['nome'])
        c.drawString(100, (x_linha - 20), "Sistema de visão")
        c.drawString(250, (x_linha - 20), "Sensor de conferência")
        c.drawString(400, (x_linha - 20), "Diferença")
        c.drawString(100, (x_linha - 22), "__________________________________________________________")

        # Dados
        c.drawString(100, (x_linha - 40), str(linha['sv']))
        c.drawString(250, (x_linha - 40), str(linha['esteira']))
        c.drawString(400, (x_linha - 40), str(linha['diferenca']))
        
        x_linha -= 100

    c.showPage()
    c.save()
