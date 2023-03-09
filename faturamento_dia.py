import json

faturamento=[]
with open("dados.json") as meu_json:
    dados = json.load(meu_json)

for i in dados:
    faturamento.append(i['valor'])

maior_que_media=[]
dia_maior_que_media=[]
total=0
maximo=0
dia_maximo=0
minimo=faturamento[0]
dia_minimo=1
j=0
dia= 0

for i in range(len(faturamento)):
    if faturamento[i] > 0:
        total = total + faturamento[i]
        dia = dia+1
    
media=total/dia

for i in range(len(faturamento)):
    if faturamento[i] > media:
        maior_que_media.append(faturamento[i])
        dia_maior_que_media.append(i+1)
        j=j+1

for i in range(len(faturamento)):
    if faturamento[i] > maximo:
        maximo = faturamento[i]
        dia_maximo = i+1
    if faturamento[i] < minimo and faturamento[i] >0:
        minimo = faturamento[i]
        dia_minimo = i+1

print("O menor valor de faturamento ocorrido em um dia do mês foi de", minimo, "no dia", dia_minimo)
print("O maior valor de faturamento ocorrido em um dia do mês foi de", maximo, "no dia", dia_maximo)
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi", j)
print("com os valores de",maior_que_media,"respectivamente nos dias", dia_maior_que_media)
print("a média foi" ,media)