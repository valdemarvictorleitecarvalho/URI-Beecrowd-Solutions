instancias = int(input())

while instancias > 0:
      bonus_aplicado = int(input())
      player_1 = [int(x) for x in input().split()]
                  
      ataque_1 = player_1[0]
      defesa_1 = player_1[1]
      level_1 = player_1[2]
                                          
      player_2 = [int(x) for x in input().split()]
                                                      
      ataque_2 = player_2[0]
      defesa_2 = player_2[1]
      level_2 = player_2[2]
                                                                              
      valor_golpe_1 = (ataque_1 + defesa_1) / 2
                                                                                          
      if level_1 % 2 == 0:
         valor_golpe_1 += bonus_aplicado
                                                                                                               
      valor_golpe_2 = (ataque_2 + defesa_2) / 2
                                                                                                                           
      if level_2 % 2 == 0:
         valor_golpe_2 += bonus_aplicado

      if valor_golpe_1 == valor_golpe_2:
         print(f"Empate")
      elif valor_golpe_1 > valor_golpe_2:
         print(f"Dabriel")
      elif valor_golpe_2 > valor_golpe_1:
         print(f"Guarte")
                                                
      instancias -= 1   
