while True:
    try:
        senha = int(input())

        senha -= 1

        print(senha)

    except EOFError:
        break
