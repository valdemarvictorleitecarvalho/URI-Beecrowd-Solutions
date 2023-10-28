def calcular_tempo():
    segundos_inicio = seg_1 + min_1 * 60 + hora_1 * 60 * 60 + data_inicio * 60 * 60 * 24
    segundos_final = seg_2 + min_2 * 60 + hora_2 * 60 * 60 + data_final * 60 * 60 * 24
    tempo_evento = segundos_final - segundos_inicio

    dias = tempo_evento // (60 * 60 * 24)
    segundos_restantes = tempo_evento % (60 * 60 * 24)
    horas = segundos_restantes // (60 * 60)
    segundos_restantes = segundos_restantes % (60 * 60)
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60

    return segundos, minutos, horas, dias

data_inicio = int(input().split()[1])
hora_inicio = input().split()
hora_1 = int(hora_inicio[0])
min_1 = int(hora_inicio[2])
seg_1 = int(hora_inicio[4])

data_final = int(input().split()[1])
hora_final = input().split()
hora_2 = int(hora_final[0])
min_2 = int(hora_final[2])
seg_2 = int(hora_final[4])

resultado = calcular_tempo()

print(f"{resultado[3]} dia(s)")
print(f"{resultado[2]} hora(s)")
print(f"{resultado[1]} minuto(s)")
print(f"{resultado[0]} segundo(s)")