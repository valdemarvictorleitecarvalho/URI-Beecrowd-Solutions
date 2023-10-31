XY = input().split()
X = int(XY[0])
Y = int(XY[1])

a = 1

for c in range(1, Y + 1):
    if a == X:
       print(c)
       a = 1
    else:
       print(c, end = " ")
       a += 1
