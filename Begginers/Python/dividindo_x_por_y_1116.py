N = int(input())

for c in range(N):
    XY = input().split()
    X = int(XY[0])
    Y = int(XY[1])
    if Y == 0:
       print(f"divisao impossivel")
    else:
       resultado = X / Y
       print(f"{resultado:.1f}")