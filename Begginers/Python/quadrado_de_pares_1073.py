n = int(input())

for c in range(1, n + 1):
    if c % 2 == 0:
       quadrado = c * c
       print(f"{c}^2 = {quadrado}")