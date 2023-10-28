linha = input().split()

a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

maiorab = (a + b + abs(a - b)) / 2
maiorc = int((maiorab + c + abs(maiorab - c)) / 2)

print(f"{maiorc} eh o maior")