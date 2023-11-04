while True:
    try:
        numero_lesmas = input()
        velocidades = input().split()
        velocidadesint = [int(x) for x in velocidades]

        mais_veloz = max(velocidadesint)

        if mais_veloz < 10:
           print("1")
        elif mais_veloz >= 10 and mais_veloz < 20:
           print("2")
        elif mais_veloz >= 20:
           print("3")
                                                                                                   
    except EOFError:                                                                                        
        break
