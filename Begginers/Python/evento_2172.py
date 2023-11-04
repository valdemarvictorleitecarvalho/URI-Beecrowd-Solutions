while True:
      entrada = input().split()
      multiplicador = int(entrada[0])
      xp = int(entrada[1])
                        
      if multiplicador == 0 and xp == 0: break
      else:
         xp *= multiplicador
         print(xp)
