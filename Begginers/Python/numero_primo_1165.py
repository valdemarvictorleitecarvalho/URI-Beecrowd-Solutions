entrada = int(input())

for j in range(entrada):
    N = int(input())
    lista = []
    
    for i in range(2, N + 1):
        if N % i == 0:
           lista.append(i)
           
    if len(lista) > 1:
       print(f"{N} nao eh primo")
    else:
       print(f"{N} eh primo")
