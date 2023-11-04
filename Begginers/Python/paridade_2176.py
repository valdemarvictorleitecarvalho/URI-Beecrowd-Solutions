binario = input()
valor_1 = 0

for num in binario:
    if num == "1":
       valor_1 += 1
               
if valor_1 % 2 == 0:
   binario += "0"
else:
   binario += "1"
                        
print(binario)
