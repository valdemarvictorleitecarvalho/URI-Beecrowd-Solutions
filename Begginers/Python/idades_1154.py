soma = 0
idade = 0

while True:
    entrada = int(input())
    
    if entrada < 0:
        break
    
    if entrada > 0:
        idade += entrada
        soma += 1

media = idade / soma if soma > 0 else 0 
print(f"{media:.2f}")