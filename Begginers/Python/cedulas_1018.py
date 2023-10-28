valores = [100, 50, 20, 10, 5, 2, 1]
numero = int(input())

print(f"{numero}")

for nota in valores:
    print(f'{int(numero / nota)} nota(s) de R$ {nota},00')
    numero %= nota