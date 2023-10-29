X = int(input())
Z = int(input())
soma = X
num = 1

while X >= Z:
      Z = int(input())
      
while soma <= Z:
      X += 1
      soma += X
      num += 1

print(num)