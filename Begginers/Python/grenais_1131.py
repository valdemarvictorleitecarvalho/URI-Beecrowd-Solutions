vgremio = 0
vinter = 0
empate = 0
grenais = 0

placar = input().split()
inter = int(placar[0])
gremio = int(placar[1])
if gremio > inter:
     vgremio += 1
elif inter > gremio:
     vinter += 1
elif gremio == inter:
     empate += 1
grenais += 1

while True:
      print(f"Novo grenal (1-sim 2-nao)")
      resposta = int(input())
      if resposta == 1:
         grenais +=1
         placar = input().split()
         inter = int(placar[0])
         gremio = int(placar[1])
         if gremio > inter:
            vgremio += 1
         elif inter > gremio:
            vinter += 1
         elif gremio == inter:
            empate += 1
      elif resposta == 2:
           break
      
print(f"{grenais} grenais")
print(f"Inter:{vinter}")
print(f"Gremio:{vgremio}")
print(f"Empates:{empate}")

if vinter > vgremio:
   print(f"Inter venceu mais")
elif vgremio > vinter:
   print(f"Gremio vence mais")
elif vgremio == vinter:
   print(f"Nao houve vencedor")