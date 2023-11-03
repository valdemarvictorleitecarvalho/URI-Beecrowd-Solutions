try:
    while True:
        reclamou = int(input())

        if reclamou == 0:
            print("vai ter copa!")
        else:
            print("vai ter duas!")
except EOFError:
    pass
