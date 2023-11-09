linhas, colunas = map(int, input().split())
matriz = []

for i in range(linhas):
    matriz.append(list(map(int, input().split())))

condicao_atendida, indice_linha, indice_coluna = 0, 0, 0

for i in range(1, linhas - 1):
    for j in range(1, colunas - 1):
        if matriz[i][j] == 42:
            if (
                matriz[i - 1][j - 1] == 7
                and matriz[i - 1][j] == 7
                and matriz[i - 1][j + 1] == 7
                and matriz[i][j - 1] == 7
                and matriz[i][j + 1] == 7
                and matriz[i + 1][j - 1] == 7
                and matriz[i + 1][j] == 7
                and matriz[i + 1][j + 1] == 7
            ):
                condicao_atendida = 1
                indice_linha, indice_coluna = i + 1, j + 1

print(f"{indice_linha} {indice_coluna}")
