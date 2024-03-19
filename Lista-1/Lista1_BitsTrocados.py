notas = [50, 10, 5, 1]
res = [0, 0, 0, 0]
valores = 0

while True:
    valor = int(input())
    if valor == 0:
        break
    valores += 1
    for i in range(4):
        res[i] = valor // notas[i]
        valor = valor % notas[i]

    print("Teste", valores)
    print(res[0], res[1], res[2], res[3])
    print()