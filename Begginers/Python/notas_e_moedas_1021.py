num = float(input())

nota_100 = num // 100
num = num - (nota_100 * 100)

nota_50 = num // 50
num = num - (nota_50 * 50)

nota_20 = num // 20
num = num - (nota_20 * 20)

nota_10 = num // 10
num = num - (nota_10 * 10)

nota_5 = num // 5
num = num - (nota_5 * 5)

nota_2 = num // 2
num = num - (nota_2 * 2)

moeda_1 = num // 1
num = num - (moeda_1 * 1)
moeda_1 = round(moeda_1, 2)
num = round(num, 2)

moeda_0_50 = num // 0.5
num = num - (moeda_0_50 * 0.5)
moeda_0_50 = round(moeda_0_50, 2)
num = round(num, 2)

moeda_0_25 = num // 0.25
num = num - (moeda_0_25 * 0.25)
moeda_0_25 = round(moeda_0_25, 2)
num = round(num, 2)

moeda_0_10 = num // 0.10
num = num - (moeda_0_10 * 0.10)
moeda_0_10 = round(moeda_0_10, 2)
num = round(num, 2)

moeda_0_05 = num // 0.05
num = num - (moeda_0_05 * 0.05)
moeda_0_05 = round(moeda_0_05, 2)
num = round(num, 2)

moeda_0_01 = num * 100
moeda_0_01 = round(moeda_0_01, 2)
num = round(num, 2)

print("NOTAS:")
print(f"{int(nota_100)} nota(s) de R$ 100.00")
print(f"{int(nota_50)} nota(s) de R$ 50.00")
print(f"{int(nota_20)} nota(s) de R$ 20.00")
print(f"{int(nota_10)} nota(s) de R$ 10.00")
print(f"{int(nota_5)} nota(s) de R$ 5.00")
print(f"{int(nota_2)} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{int(moeda_1)} moeda(s) de R$ 1.00")
print(f"{int(moeda_0_50)} moeda(s) de R$ 0.50")
print(f"{int(moeda_0_25)} moeda(s) de R$ 0.25")
print(f"{int(moeda_0_10)} moeda(s) de R$ 0.10")
print(f"{int(moeda_0_05)} moeda(s) de R$ 0.05")
print(f"{int(moeda_0_01)} moeda(s) de R$ 0.01")