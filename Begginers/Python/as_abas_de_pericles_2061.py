entrada = input().split()

abas = int(entrada[0])
acoes = int(entrada[1])

while acoes > 0:
      
      ato = input()
                  
      if ato == "fechou":
         abas += 1
                                          
      if ato == "clicou":
         abas -= 1
                                                                  
      acoes -= 1
                                                                              
print(abas)
