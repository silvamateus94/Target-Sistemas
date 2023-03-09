n = int(input("Entre com o número que deseja verificar: "))
ultimo = 1
penultimo = 0
termo = 0

if (n==0) or (n==1):
    print("Pertence a Sequência de Fibonnaci")
else:
    while termo < n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
    if termo == n:
        print("Pertence a Sequência de Fibonnaci")
    else:
        print("NÃO Pertence a Sequência de Fibonnaci")