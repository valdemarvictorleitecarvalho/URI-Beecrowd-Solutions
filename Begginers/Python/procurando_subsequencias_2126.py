caso = 1

while True:
    try:
        qtd = 0
        substring = input()
        string = input()

        len_string = len(string)
        len_substring = len(substring)
                                                    
        pos = -1

        for i in range(len_string - len_substring + 1):
            j = 0

            while j < len_substring and string[i + j] == substring[j]:
                j += 1

            if j == len_substring:
               qtd += 1
               pos = i + 1

        if qtd != 0:
           print(f"Caso #{caso}:")
           print(f"Qtd.Subsequencias: {qtd}")
           print(f"Pos: {pos}")
        else:
           print(f"Caso #{caso}:")
           print(f"Nao existe subsequencia")
                                                               
        print(f"")
                                                                                  
        caso += 1

    except EOFError:
        break
