from math import sqrt

while True:
    medidas = input().split()
    A = int(medidas[0])
            
    if A == 0: break
                    
    B = int(medidas[1])
    C = int(medidas[2])
                                
    lado = int(sqrt(((A * B / C) * 100.0)))
                                        
    print(lado)
