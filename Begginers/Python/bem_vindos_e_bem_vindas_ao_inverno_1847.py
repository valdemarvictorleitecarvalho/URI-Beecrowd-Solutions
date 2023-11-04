def humor(dias):
    dia_1 = int(dias[0])
    dia_2 = int(dias[1])    
    dia_3 = int(dias[2])

    if dia_1 > dia_2:
       if dia_3 > dia_2:
          return True
       else:
          if dia_2 - dia_3 < dia_1 - dia_2:
             return True
          else:
             return False
    elif dia_1 < dia_2:
         if dia_3 < dia_2:
            return False
         else:
            if dia_2 - dia_3 > dia_1 - dia_2:
               return False
            else:
               return True

    else:
       if dia_3 > dia_1:
          return True
       else:
          return False
                                               
dias = input().split()

if humor(dias):
   print(f":)")
else:
   print(f":(")
