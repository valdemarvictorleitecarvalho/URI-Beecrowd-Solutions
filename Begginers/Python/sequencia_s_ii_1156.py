I = 3
D = 2
S = 1

while I <= 39:
    S = S + I / D
    I += 2
    D *= 2

print(f"{S:.2f}")
