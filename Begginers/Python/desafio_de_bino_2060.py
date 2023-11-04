qt_numeros = int(input())
lista = [int(x) for x in input().split()]

multiplo_2 = 0
multiplo_3 = 0
multiplo_4 = 0
multiplo_5 = 0

for num in lista:
    if num % 2 == 0:
       multiplo_2 += 1
    if num % 3 == 0:
       multiplo_3 += 1
    if num % 4 == 0:
       multiplo_4 += 1
    if num % 5 == 0:
       multiplo_5 += 1
                                                   
print(f"{multiplo_2} Multiplo(s) de 2")
print(f"{multiplo_3} Multiplo(s) de 3")
print(f"{multiplo_4} Multiplo(s) de 4")
print(f"{multiplo_5} Multiplo(s) de 5")
