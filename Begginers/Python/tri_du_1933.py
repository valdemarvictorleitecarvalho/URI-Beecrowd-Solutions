cartas = input().split()
A = int(cartas[0])
B = int(cartas[1])

if A == B:
   print(A)
elif A != B:
   if A > B:
      print(A)
   elif A < B:
      print(B)
