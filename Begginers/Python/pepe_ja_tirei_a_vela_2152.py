testes = int(input())

while testes > 0:
    entrada = input().split()
    hora = int(entrada[0])  
    minuto = int(entrada[1])
    ocorrencia = int(entrada[2])

    if ocorrencia == 1:
       print(f"{hora:02d}:{minuto:02d} - A porta abriu!")
    else:
       print(f"{hora:02d}:{minuto:02d} - A porta fechou!")

    testes -= 1
