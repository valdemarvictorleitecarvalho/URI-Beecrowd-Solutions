for i in range(10):
    X = int(input())
    
    if X <= 0:
       X = 1
    else:
       X = X
    
    print(f"X[{i}] = {X}")