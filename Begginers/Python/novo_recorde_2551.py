while True:
    try:
        testes = int(input())
                    
        dia = 1
        maior = 0
        while testes > 0:
              corrida = input().split()
                                                                        
              tempo = int(corrida[0])
              distancia = int(corrida[1])
                                                                                                                  
              velocidade_media = distancia / tempo
                                                                                                                                              
              if velocidade_media > maior:
                 maior = velocidade_media
                 print(dia)

              dia += 1
              testes -= 1

    except EOFError:
        break
