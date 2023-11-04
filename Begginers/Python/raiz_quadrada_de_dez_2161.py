num = float(input())
valor = 0.0

while num > 0:
    valor += 6.0
    valor = 1.0 / valor
    num -= 1

valor += 3.0

print(f"{valor:.10f}")
