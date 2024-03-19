n,m = input().split()
n = int(n)
m = int(m)

#Crio um vetor para todas as pedras inicializado já com 0
n = n +1
pedras = [0] * n #Faço n +1 pois o vetor inicia na posição 0, mas quero usar os índices de 1 até n (inclusive).

for _ in range(m): #Para cada sapo, leio a posição inicial dele e também a distância do pulo
    p,d = input().split()
    p = int(p)
    d = int(d)
    
    #Para cada sapo lido, faço marco todas as casas que consido alcançar movendo para a esquerda ou direita 
    for i in range(p, n, d): #Aqui faço o sapo mover para a direita, de d em d, iniciando na pedra p até a pedra n-1
        pedras[i] = 1

    for i in range(p, 0, -d): #Aqui faço o sapo mover para a esquerda, de d em d, iniciando na pedra p até a pedra 1
        pedras[i] = 1

#Aqui simplesmente imprimo a situação das pedras alcançadas ou não pelos sapos
for i in range(1, n):
    print("%d" % (pedras[i]))

