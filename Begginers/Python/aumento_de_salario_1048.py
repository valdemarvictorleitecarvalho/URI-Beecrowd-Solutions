salario = float(input())

if 0 <= salario <= 400:
   reajuste = salario * 0.15
   salariofinal = salario + reajuste
   print(f"Novo salario: {salariofinal:.2f}")
   print(f"Reajuste ganho: {reajuste:.2f}")
   print(f"Em percentual: 15 %")
elif 400.1 <= salario <= 800:
   reajuste = salario * 0.12
   salariofinal = salario + reajuste
   print(f"Novo salario: {salariofinal:.2f}")
   print(f"Reajuste ganho: {reajuste:.2f}")
   print(f"Em percentual: 12 %")
elif 800.01 <= salario <= 1200:
   reajuste = salario * 0.10
   salariofinal = salario + reajuste
   print(f"Novo salario: {salariofinal:.2f}")
   print(f"Reajuste ganho: {reajuste:.2f}")
   print(f"Em percentual: 10 %")
elif 1200.01 <= salario <= 2000:
   reajuste = salario * 0.07
   salariofinal = salario + reajuste
   print(f"Novo salario: {salariofinal:.2f}")
   print(f"Reajuste ganho: {reajuste:.2f}")
   print(f"Em percentual: 7 %")
elif salario > 2000:
   reajuste = salario * 0.04
   salariofinal = salario + reajuste
   print(f"Novo salario: {salariofinal:.2f}")
   print(f"Reajuste ganho: {reajuste:.2f}")
   print(f"Em percentual: 4 %")