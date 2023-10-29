N = int(input())
primeiro = 1
segundo = 1
terceiro = 1
quadrado = 1
cubo = 1

for i in range(N):
    print(f"{primeiro} {quadrado} {cubo}")
    primeiro += 1
    segundo += 1
    quadrado = (segundo ** 2)
    terceiro += 1
    cubo = (terceiro ** 3)