n = int(input())

for c in range(n):
    x = int(input())
    if x == 0:
       print(f"NULL")
    elif x % 2 == 0 and x > 0:
         print(f"EVEN POSITIVE")
    elif x % 2 == 0 and x < 0:
         print(f"EVEN NEGATIVE")
    elif x % 2 != 0 and x > 0:
         print(f"ODD POSITIVE")
    elif x % 2 != 0 and x < 0:
         print(f"ODD NEGATIVE")