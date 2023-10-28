valores = input().split()
n1 = int(valores[0])
n2 = int(valores[1])

if n2 % n1 == 0 or n1 % n2 == 0:
    print(f"Sao Multiplos")
else:
    print(f"Nao sao Multiplos")