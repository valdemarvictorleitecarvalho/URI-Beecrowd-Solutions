T = int(input())

for i in range(0, T):
    pop_a, pop_b, g1, g2 = map(float, input().split())
    pop_a = int(pop_a)
    pop_b = int(pop_b)
    anos = 0
   
    while pop_b >= pop_a:
        pop_a = int(pop_a * (1 + g1 / 100))
        pop_b = int(pop_b * (1 + g2 / 100))
        anos = anos + 1
        
        if anos >= 101:
            print(f"Mais de 1 seculo.")
            break
    
    if anos <= 100:
        anos = int(anos)
        print(f"{anos} anos.")
