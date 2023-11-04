def jogo(sheldon, raj):
    
    if sheldon == raj:
       return None
    elif sheldon == "tesoura" and raj == "papel":
         return True
    elif sheldon == "papel" and raj == "pedra":
         return True
    elif sheldon == "pedra" and raj == "lagarto":
         return True
    elif sheldon == "lagarto" and raj == "Spock":
         return True
    elif sheldon == "Spock" and raj == "tesoura":
         return True
    elif sheldon == "tesoura" and raj == "lagarto":
         return True
    elif sheldon == "lagarto" and raj == "papel":
         return True
    elif sheldon == "papel" and raj == "Spock":
         return True
    elif sheldon == "Spock" and raj == "pedra":
         return True
    elif sheldon == "pedra" and raj == "tesoura":
         return True
    else:
         return False

testes = int(input())
caso = 1

while caso < testes + 1:
      jogada = input().split()
      sheldon = jogada[0]
      raj = jogada[1]
                        
      if jogo(sheldon, raj):
         print(f"Caso #{caso}: Bazinga!")
      elif jogo(sheldon, raj) == False:
           print(f"Caso #{caso}: Raj trapaceou!")
      elif jogo(sheldon, raj) == None:
           print(f"Caso #{caso}: De novo!")
                                                                               
      caso += 1
