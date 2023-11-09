import math

while True:
    try:
        x1, y1, x2, y2, v, r1, r2 = map(float, input().split())
        X = (x2 - x1) ** 2
        Y = (y2 - y1) ** 2
        
        distancia = math.sqrt(X + Y)
        distancia += v * 1.50
        range = r1 + r2
       
        if distancia > range:
            print("N")
        else:
            print("Y")
    except EOFError:
        break
