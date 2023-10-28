p = 0
i = 0
pos = 0
neg = 0

for calc in range(5):
    x = int(input())
    if x % 2 == 0:
       p += 1
    elif x % 2 != 0:
       i += 1
    if x > 0:
       pos += 1
    elif x < 0:
       neg += 1

print(f"{p} valor(es) par(es)")
print(f"{i} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")