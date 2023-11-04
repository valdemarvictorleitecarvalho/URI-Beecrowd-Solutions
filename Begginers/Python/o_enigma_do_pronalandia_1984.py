sequencia = input().strip()
sequencia_invertida = ""

for i in range(len(sequencia) -1, -1, -1):
    sequencia_invertida += sequencia[i] 

print(f"{sequencia_invertida}")
