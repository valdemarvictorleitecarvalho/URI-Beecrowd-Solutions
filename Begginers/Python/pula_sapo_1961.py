jogada = input().split()
altura = int(jogada[0])

canos = input().split()
canos_int = [int(x) for x in canos]

for i in range(len(canos) - 1):
    diferenca = abs(canos_int[i + 1] - canos_int[i])
    if diferenca <= altura:
       ganhou = True
    else:
       ganhou = False
       break
                                    
if ganhou:
   print(f"YOU WIN")
else:
   print(f"GAME OVER")
