num = int(input())
lista = []

for k in range(num + 1):
    entrada = [int(x) for x in input().split()]
    lista.append(entrada)

for i in range(num):
    for j in range(num):
        if lista[i][j] + lista[i][j + 1] + lista[i + 1][j] + lista[i + 1][j + 1] < 2:
           print("U", end="")
        else:
           print("S", end="")
                                                      
    print()
