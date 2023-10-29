N = int(input())

if N == 0:
   print(f"1")
elif N > 0:
   x = 1
   for i in range(1, N + 1):
       x *= i
       
print(x)