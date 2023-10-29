while True:
      XY = input().split()
      X = int(XY[0])
      Y = int(XY[1])
      if X > 0 and Y > 0:
         print(f"primeiro")
      elif X < 0 and Y > 0:
         print(f"segundo")
      elif X < 0 and Y < 0:
         print(f"terceiro")
      elif X > 0 and Y < 0:
         print(f"quarto")
      else:
           break