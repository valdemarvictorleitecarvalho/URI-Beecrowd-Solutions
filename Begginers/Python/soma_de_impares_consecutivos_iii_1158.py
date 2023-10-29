N = int(input())

for i in range(N):
    soma = 0
    XY = input().split()
    X = int(XY[0])
    Y = int(XY[1])
        
    if X % 2 == 0:
       X += 1 
        
    for c in range(0, Y):
        soma += X
        X += 2
    
    print(soma)