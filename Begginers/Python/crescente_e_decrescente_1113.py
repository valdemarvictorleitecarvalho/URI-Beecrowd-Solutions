while True:
      XY = input().split()
      X = int(XY[0])
      Y = int(XY[1])
      if X > Y:
         print(f"Decrescente")
      elif X < Y:
         print(f"Crescente")
      elif X == Y:break