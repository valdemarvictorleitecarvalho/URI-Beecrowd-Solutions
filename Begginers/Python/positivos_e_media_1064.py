q = 0
soma = 0

for calc in range(6):
    x = float(input())
    if x > 0:
        q += 1
        soma += x
        media = soma / q

print(f"{q} valores positivos")
print(f"{media:.1f}")