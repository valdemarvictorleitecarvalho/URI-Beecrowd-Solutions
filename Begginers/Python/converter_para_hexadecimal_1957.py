numero = int(input())
convertido = ""
lista = []
hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

while numero:
    lista.append(hexa[numero % 16])
    numero //= 16

for i in range(len(lista) - 1, -1, -1):
    convertido += lista[i]
                
print(convertido)
