testes = int(input())

while testes != 0:
      jogada = input().split()
      numeros = input().split()

      numeros_int = [int(x) for x in numeros]

      soma = 0
      for num in numeros_int:
          soma += num
                                              
      par = None
      if soma % 2 == 0:
         par = True
                                                                            
      if par:
         indice = jogada.index("PAR") - 1
         print(jogada[indice])
      else:
         indice = jogada.index("IMPAR") - 1
         print(jogada[indice])
                                                                                                                                     
      testes -= 1
