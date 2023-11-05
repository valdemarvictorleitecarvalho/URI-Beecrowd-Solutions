medidas = int(input())
alturas = [int(x) for x in input().split()]
condicao = 1

if medidas == 2 and alturas[0] == alturas[1]:
   condicao = 0
else:
   for i in range(2, medidas):
       if alturas[i] >= alturas[i - 1] and alturas[i - 1] >= alturas[i - 2] or alturas[i] <= alturas[i - 1] and alturas[i - 1] <= alturas[i - 2]:
          condicao = 0
          break

if condicao == 1:
   print(f"1")
else:
   print(f"0")
