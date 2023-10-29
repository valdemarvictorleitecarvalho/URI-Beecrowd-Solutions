N = int(input())

for c in range(N):
    XY = input().split()
    X = int(XY[0])
    Y = int(XY[1])
    contador = 0

    if X > Y:
       for i in range(Y + 1, X):
           if i % 2 != 0:
              contador += i
    elif Y > X:
       for i in range(X + 1, Y):
           if i % 2 != 0:
              contador += i
    print(contador)