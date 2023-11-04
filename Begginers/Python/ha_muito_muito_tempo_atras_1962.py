num_testes = int(input())

while num_testes > 0:
      anos = int(input())
            
      transcorrido = 2015 - anos
                        
      if transcorrido > 0:
         print(f"{transcorrido} D.C.")
      elif transcorrido == 0:
           print(f"1 A.C.")
      elif transcorrido < 0:
           transcorrido = abs(transcorrido)
           transcorrido += 1
           print(f"{transcorrido} A.C.")
                                                                                                          
      num_testes -= 1
