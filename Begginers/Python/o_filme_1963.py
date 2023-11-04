valores = input().split()

preco_antes = float(valores[0])
preco_depois = float(valores[1])

aumento = ((preco_depois - preco_antes) / preco_antes) * 100

print(f"{aumento:.2f}%")
