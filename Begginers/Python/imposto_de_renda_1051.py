salario = float(input())

if 0 <= salario <= 2000:
   print(f"Isento")
elif 2000 < salario <= 3000:
   valor = (salario - 2000) * 0.08
   print(f"R$ {valor:.2f}")
elif 3000 < salario <= 4500:
   valor = (salario - 3000) * 0.18 + (1000 * 0.08)
   print(f"R$ {valor:.2f}")
elif salario > 4500:
   valor = (salario - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
   print(f"R$ {valor:.2f}")