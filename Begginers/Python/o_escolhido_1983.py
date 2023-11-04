quantidade_alunos = int(input())
candidatos_validos = 0
maior_nota = 0
representante = None

while quantidade_alunos > 0:
      candidatura = input().split()
      aluno = candidatura[0]
      nota = float(candidatura[1])
                        
      if nota >= 8:
         candidatos_validos += 1
         if nota > maior_nota:
            maior_nota = nota
            representante = aluno
                                                                              
      quantidade_alunos -= 1
                                                                                          
if candidatos_validos > 0:
   print(representante)
else:
   print(f"Minimum note not reached")
