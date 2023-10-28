import math 

n = list(map(float, input().split()))

n.sort(reverse = True)

A = float(n[0])
B = float(n[1])
C = float(n[2])

if A >= B + C:
   print(f"NAO FORMA TRIANGULO")
else:
   if A == math.sqrt((B * B) + (C * C)):
      print(f"TRIANGULO RETANGULO")
   elif A > math.sqrt((B * B) + (C * C)):
      print(f"TRIANGULO OBTUSANGULO")
   elif A < math.sqrt((B * B) + (C * C)):
      print(f"TRIANGULO ACUTANGULO")
      
if A == B == C and not A >= B + C:
   print(f"TRIANGULO EQUILATERO")
elif A == B or A == C or B == C:
   print(f"TRIANGULO ISOSCELES")