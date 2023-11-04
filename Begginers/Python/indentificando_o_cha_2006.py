T = input()
respostas = input().split()
acertou = 0

for i in respostas:
    if T == i:
       acertou += 1
              
print(acertou)
