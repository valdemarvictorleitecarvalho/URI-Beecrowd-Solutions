testes = int(input())

while testes > 0:
      galopeira = 0.00
      palavra = input()
                  
      for letra in range(len(palavra)):
          galopeira += 0.01
                                        
      print(f"{galopeira:.2f}")
                                                    
      testes -= 1
