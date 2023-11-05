matriz = [[0 for coluna in range(12)] for linha in range(12)]

linha_entrada = int(input())
operacao = input()
resultado = 0.0

for linha in range(12):
    for icol in range(12):
        matriz[linha][icol] = float(input())
        if linha == linha_entrada:
           resultado += matriz[linha_entrada][icol]
                                          
if operacao == "S":
   print(f"{resultado:.1f}")
elif operacao == "M":
   resultado /= 12
   print(f"{resultado:.1f}")
