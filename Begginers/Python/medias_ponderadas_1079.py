n = int(input())

for calc in range(n):
    x = input().split()
    x1 = float(x[0])
    x2 = float(x[1])
    x3 = float(x[2])
    media = (((x1 * 2) + (x2 * 3) + (x3 * 5)) / 10)
    print(f"{media:.1f}")