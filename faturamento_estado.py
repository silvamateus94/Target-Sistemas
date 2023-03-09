faturamento = [67836.43 , 36678.66 , 29229.88 , 7165.48 , 19849.53]
estado = ["SP", "RJ" , "MG" , "ES" , "outro"]
total=0


for i in range(len(faturamento)):
    total = total + faturamento[i]

for i in range(len(estado)):
    faturamento[i] = faturamento[i]*100/total
    print(estado[i], "representa" , faturamento[i]," % em relação ao percentual total de vendas")