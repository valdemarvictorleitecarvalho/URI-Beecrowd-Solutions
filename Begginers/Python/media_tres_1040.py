notas = input().split()
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print(f"Media: {media:.1f}")

if media >= 7:
   print(f"Aluno aprovado.")
elif media < 5:
   print(f"Aluno reprovado.")
elif 5 <= media < 7:
   print(f"Aluno em exame.")
   
if 5 <= media < 7:
   notaexame = float(input())
   print(f"Nota do exame: {notaexame:.1f}")
   mediafinal = (media + notaexame) / 2
   if mediafinal > 5:
      print(f"Aluno aprovado.")
   else:
      print(f"Aluno reprovado.")
   print(f"Media final: {mediafinal:.1f}")