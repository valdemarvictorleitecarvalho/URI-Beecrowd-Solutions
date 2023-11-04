creditos = input().split()

A = int(creditos[0])
B = int(creditos[1])
C = int(creditos[2])

if A == B or B == C or C == A:
   print(f"S")
elif A + B == C or A + C == B or B + C == A:
   print(f"S")
else:
   print(f"N")
