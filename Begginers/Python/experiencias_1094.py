testes = int(input())
somacobaias = 0
somacoelhos = 0
somaratos = 0
somasapos = 0

for c in range(testes):
    x = input().split()
    x[0] = float(x[0])
    quantidade = x[0]
    tipo = x[1]
    somacobaias += quantidade
    if tipo == "C":
       somacoelhos += quantidade
    elif tipo == "R":
       somaratos += quantidade
    elif tipo == "S":
       somasapos += quantidade
pcoelhos = 100 - (((somacobaias - somacoelhos) * 100) / somacobaias)
pratos = 100 - (((somacobaias - somaratos) * 100) / somacobaias)
psapos = 100 - (((somacobaias - somasapos) * 100) / somacobaias)

print(f"Total: {somacobaias:.0f} cobaias") 
print(f"Total de coelhos: {somacoelhos:.0f}")
print(f"Total de ratos: {somaratos:.0f}")
print(f"Total de sapos: {somasapos:.0f}")
print(f"Percentual de coelhos: {pcoelhos:.2f} %")
print(f"Percentual de ratos: {pratos:.2f} %")
print(f"Percentual de sapos: {psapos:.2f} %")