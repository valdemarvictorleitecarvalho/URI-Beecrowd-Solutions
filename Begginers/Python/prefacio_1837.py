entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])

for r in range(abs(b)):
    if (a - r) % b == 0:
       q = int((a - r) / b)
       break

print(q, r)
