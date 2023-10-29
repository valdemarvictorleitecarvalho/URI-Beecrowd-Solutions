soma = 0
valor = input().split()
A = int(valor[0])
ultimo = len(valor) - 1
N = int(valor[ultimo])

for i in range(0, N):
    soma += A + i
    
print(soma)