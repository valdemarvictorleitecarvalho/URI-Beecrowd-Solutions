xy = input().split()
x = float(xy[0])
y = float(xy[1])

if x == y == 0:
   print(f"Origem")
elif x == 0 and y > 0 or x == 0 and y < 0:
   print(f"Eixo Y")
elif y == 0 and x > 0 or y == 0 and x < 0:
   print(f"Eixo X")
elif x > 0 and y > 0:
   print(f"Q1")
elif x > 0 and y < 0:
   print(f"Q4")
elif x < 0 and y > 0:
   print(f"Q2")
elif x < 0 and y < 0:
   print(f"Q3")