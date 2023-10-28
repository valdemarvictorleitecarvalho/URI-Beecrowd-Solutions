n = int(input())

for c in range(1, 10001):
    resto = c % n
    if resto == 2:
       print(c)