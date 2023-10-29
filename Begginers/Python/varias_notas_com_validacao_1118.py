somaN = 0
notas = 0
opcao = 1

while opcao != 2:
    while notas < 2:
        N = float(input())
        if 0 <= N <= 10:
            somaN += N
            notas += 1
        else:
            print(f"nota invalida")

    media = somaN / 2
    print(f"media = {media:.2f}")

    while True:
        print(f"novo calculo (1-sim 2-nao)")
        x = int(input())
        if x == 2:
           opcao = x 
           break
        elif x == 1:
            somaN = 0
            notas = 0
            break
        else:
            continue