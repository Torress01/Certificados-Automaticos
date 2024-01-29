import openpyxl
from PIL import Image, ImageDraw, ImageFont

#Abrir a planilha
workbook_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']

for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):
    # cada célula que contém a info que precisamos
    nome_curso = linha[0].value #Nome do curso
    nome_participante = linha[1].value #Nome do participante
    tipo_participacao = linha[2].value #tipo de participacao
    data_inicio = linha[3].value # data de inicio
    data_final = linha[4].value # data final
    carga_horaria = linha[5].value # carga horaria 
    data_emissao = linha[6].value # data emissao

#Transferir os dados da planilha para a imagem do certificado
    font_nome = ImageFont.truetype('./tahomabd.ttf', 90)
    font_geral = ImageFont.truetype('./tahoma.ttf', 90)
    font_data = ImageFont.truetype('./tahomabd.ttf', 55)

    image = Image.open('./certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(image)

    desenhar.text((1020, 827), nome_participante, fill= 'black', font = font_nome)
    desenhar.text((1070, 945), nome_curso, fill= 'black', font = font_geral)
    desenhar.text((1435, 1065), tipo_participacao, fill= 'black', font = font_geral)
    desenhar.text((1480, 1182),str(carga_horaria), fill= 'black', font = font_geral)
    desenhar.text((725, 1770), data_inicio, fill= 'black', font = font_data)
    desenhar.text((725, 1925), data_final, fill= 'black', font = font_data)
    desenhar.text((2190, 1925),data_emissao, fill= 'black', font = font_data)

    image.save(f'./{indice} {nome_participante} certificado.png')