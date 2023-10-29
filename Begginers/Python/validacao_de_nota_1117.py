somaN = 0 
notas = 0

while notas < 2:
      N = float(input())
      if 0 <= N <= 10:
         somaN += N
         notas += 1
      else:
         print(f"nota invalida")
      
media = somaN / 2
print(f"media = {media:.2f}")