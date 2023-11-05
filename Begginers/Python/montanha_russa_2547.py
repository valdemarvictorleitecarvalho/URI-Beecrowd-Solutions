while True:
    try:
        entrada = input().split()
        visitantes = int(entrada[0])
        altura_minima = int(entrada[1])
        altura_maxima = int(entrada[2])

        pode = 0

        while visitantes > 0:
              altura = int(input())
                                                                        
              if altura >= altura_minima and altura <= altura_maxima:
                 pode += 1
                                                                                                                
              visitantes -= 1
                                                                                                                                            
        print(pode)

    except EOFError:
        break
