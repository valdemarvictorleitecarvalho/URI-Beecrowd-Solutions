n = input().split()
a = float(n[0])
b = float(n[1])
c = float(n[2])

if (2 * a == 0)  or (b ** 2 - 4 * a * c) < 0:
    print("Impossivel calcular")
else:
    r1 = (-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")