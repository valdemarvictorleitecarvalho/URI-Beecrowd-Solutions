linha = input().split()

A = float(linha[0])
B = float(linha[1])
C = float(linha[2])

pi = 3.14159

triangulo = (A * C) / 2
circulo = pi * (C ** 2)
trapezio = ((A + B) * C) / 2
quadrado = B * B
retangulo = A * B

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")