alcool = 0
gasolina = 0
diesel = 0

while True:
      codigo = int(input())
      if 1 <= codigo <= 4:
         if codigo == 1:
            alcool += 1
         elif codigo == 2:
            gasolina += 1
         elif codigo == 3:
            diesel += 1
         elif codigo == 4:
              break
       
print(f"MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")