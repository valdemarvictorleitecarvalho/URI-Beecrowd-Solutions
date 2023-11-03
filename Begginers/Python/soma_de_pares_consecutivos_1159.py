while True:
      valor = int(input())
      
      if valor == 0: break
  
      if valor % 2 == 0:
         total = 0
         for i in range(valor, valor + 9, 2):
             total += i
      else:
           total = 0
           for i in range(valor + 1, valor + 10, 2):
               total += i

      print(total)
