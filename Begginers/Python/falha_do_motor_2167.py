testes = int(input())
velocidades = [int(x) for x in input().split()]
indice = 0

for i in range(1, len(velocidades)):
    if velocidades[i] < velocidades[i - 1]:
       indice = i + 1
       break

print(indice)
