while True:
    try:
        mes, dia = map(int, input().split())
        termino = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 25]

        if mes == 12 and dia == 25:
           print("E natal!")
        elif mes == 12 and dia > 25:
           print("Ja passou!")
        elif mes == 12 and dia == 24:
           print("E vespera de natal!")
        else:
           dias_restantes = termino[mes - 1] - dia
                                                                                                           
           for i in range(mes, 12):
               dias_restantes += termino[i]
                                                                                                                                               
           print(f"Faltam {dias_restantes} dias para o natal!")
                                                                                                                                                              
    except EOFError:
        break
