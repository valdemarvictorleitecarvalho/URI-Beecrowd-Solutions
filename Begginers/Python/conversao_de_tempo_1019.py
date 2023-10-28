n = int(input())

horas = int(n / 3600)
r = int(n % 3600)
minutos = int(r / 60)
segundos = int(r % 60)

print(f"{horas}:{minutos}:{segundos}")