h = input().split()
inicio = int(h[0])
fim = int(h[1])

if fim > inicio:
   hora = fim - inicio
   print(f"O JOGO DUROU {hora} HORA(S)")
else: 
   hora = 24 - inicio + fim
   print(f"O JOGO DUROU {hora} HORA(S)")