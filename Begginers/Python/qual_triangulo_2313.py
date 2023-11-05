import math

triangulo = input().split()

A = int(triangulo[0])
B = int(triangulo[1])
C = int(triangulo[2])

retangulo = False
invalido = False

if A >= B + C or B >= A + C or C >= A + B:
    print(f"Invalido")
    invalido = True
else:
    if A == B == C:
       print(f"Valido-Equilatero")
    elif A == B or A == C or B == C:
       print(f"Valido-Isoceles")
    else:
       print(f"Valido-Escaleno")

    if A == math.sqrt(B**2 + C**2) or B == math.sqrt(A**2 + C**2) or C == math.sqrt(A**2 + B**2):
       retangulo = True

if not invalido:
   if retangulo:
      print(f"Retangulo: S")
   else:
      print(f"Retangulo: N")
