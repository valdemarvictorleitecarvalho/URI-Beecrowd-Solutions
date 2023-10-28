n = input().split()

a = float(n[0])
b = float(n[1])
c = float(n[2])

if a + b > c and b + c > a and a + c > b:
   perimetro = a + b + c
   print(f"Perimetro = {perimetro:.1f}")
else: 
   trapezio = ((a + b) * c) / 2
   print(f"Area = {trapezio:.1f}")