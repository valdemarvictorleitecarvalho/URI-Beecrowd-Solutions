num_competidores = int(input())

while num_competidores > 0:
    competidor = input()
    dificuldade = float(input())

    notas = [float(x) for x in input().split()]

    maior = notas[0]
    menor = notas[0]

    for nota in notas:
        if nota > maior:
           maior = nota
        if nota < menor:
           menor = nota

    notas.remove(maior)
    notas.remove(menor)

    pontos = sum(notas) * dificuldade

    print(f"{competidor} {pontos:.2f}")

    num_competidores -= 1
