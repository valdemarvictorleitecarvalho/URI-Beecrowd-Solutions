while True:
    try:
        entrada = input().split()
        gameplays = int(entrada[0])
        identificador = entrada[1]
        minha_gameplay = 0

        while gameplays > 0:
              videos = input().split()
                                                                
              if videos[0] == identificador and videos[1] == "0":
                 minha_gameplay += 1
                                                                                                        
              gameplays -= 1

        print(minha_gameplay)

    except EOFError:
        break
