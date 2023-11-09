conta = [7, 12, 22, 52, 102, 15, 25, 55, 105, 30, 60, 110, 70, 120, 150]

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    comparacao = M - N
    contador = 0
    for i in range(15):
        if conta[i] == comparacao:
            contador = 1
            break
    if contador:
        print("possible")
    else:
        print("impossible")
