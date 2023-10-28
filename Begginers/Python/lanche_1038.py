entrada = input().split()
code = int(entrada[0])
qt = int(entrada[1])

if code == 1:
   total = 4 * qt
   print(f"Total: R$ {total:.2f}")
elif code == 2: 
   total = 4.5 * qt
   print(f"Total: R$ {total:.2f}")
elif code == 3: 
   total = 5 * qt
   print(f"Total: R$ {total:.2f}")
elif code == 4: 
   total = 2 * qt
   print(f"Total: R$ {total:.2f}") 
elif code == 5: 
   total = 1.5 * qt
   print(f"Total: R$ {total:.2f}")