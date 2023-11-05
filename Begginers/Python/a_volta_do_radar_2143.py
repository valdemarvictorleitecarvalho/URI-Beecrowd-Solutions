while True:
    testes = int(input())
        
    if testes == 0: break
                
    for i in range(1, testes + 1):
        n = int(input())
        if n % 2 == 1:
           print(n * 2 - 1)
        else:
           print(n * 2 - 2)
