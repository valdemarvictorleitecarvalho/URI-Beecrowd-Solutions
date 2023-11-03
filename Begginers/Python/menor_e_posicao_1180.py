N = int(input())
X = input().split()
lista = [0] * N
X_int = [int(x) for x in X]

for i in range(N):  
    lista[i] = X_int[i]
    
    
menor = lista[0]
posicao = 0    
for j in range(len(lista)):
    if lista[j] < menor:
       menor = lista[j]
       posicao = j
       
print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")
