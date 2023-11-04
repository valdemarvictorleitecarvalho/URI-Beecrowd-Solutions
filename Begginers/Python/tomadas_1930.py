reguas = input().split()
reguasint = [int(x) for x in reguas]
maximo = reguasint[0]

for i in range(len(reguasint) - 1):
    conector = (maximo + reguasint[i + 1]) - 1
    maximo = conector
            
print(maximo)
