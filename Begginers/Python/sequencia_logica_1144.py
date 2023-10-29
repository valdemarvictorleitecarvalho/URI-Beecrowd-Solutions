N = int(input())

n1 = 1 

for i in range(N * 2):
    print(f"{n1} {(n1 ** 2) + (i % 2)} {(n1 ** 3) + (i % 2)}")
    n1 += (i % 2)