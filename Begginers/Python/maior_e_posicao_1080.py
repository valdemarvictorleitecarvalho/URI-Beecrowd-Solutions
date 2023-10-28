maior = 0
pos = 0

for c in range(1, 101):
    x = int(input())
    if x > maior:
        maior = x
        pos = c

print(f"{maior}")
print(f"{pos}")