while True:
    try:
        horario = input().split(':')
        calculo = int(horario[0]) * 60 + int(horario[1]) - 420
                            
        if calculo < 0:
           calculo = 0
                                                       
        print(f"Atraso maximo: {calculo}")
                                                                       
    except EOFError:
        break
