while True:
      nums = [int(x) for x in input().split()]
      minimo = min(nums)
      maximo = max(nums)
      
      if minimo <= 0:
         break
      
      soma = 0
      sequencia = ""
      for i in range(minimo, maximo + 1):
          sequencia += str(i) + " "
          soma += i
      
      print(f"{sequencia}Sum={soma}")