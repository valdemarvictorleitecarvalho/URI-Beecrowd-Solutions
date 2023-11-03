entrada = int(input())

for j in range(entrada):
    N = int(input())
    lista = []

    for i in range(1, N):
        if N % i == 0:
           lista.append(i)
       
    soma = sum(lista)

    if soma == N:
       print(f"{N} eh perfeito")
    else:
        print(f"{N} nao eh perfeito")
