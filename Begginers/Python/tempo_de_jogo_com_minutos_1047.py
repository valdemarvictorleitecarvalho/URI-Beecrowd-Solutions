entrada = input().split()
a = int(entrada[0])
c = int(entrada[1])
b = int(entrada[2])
d = int(entrada[3])

diferenca = ((b * 60) + d) - ((a * 60) + c)

if diferenca <= 0:
   diferenca += 60 * 24
    
tempo = diferenca // 60
minuto = diferenca % 60

print(f"O JOGO DUROU {tempo} HORA(S) E {minuto} MINUTO(S)")
