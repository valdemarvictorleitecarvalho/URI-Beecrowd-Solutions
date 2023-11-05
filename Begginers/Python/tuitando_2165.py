escrito = input()
contador = 0

for char in escrito:
    contador += 1
        
if contador > 140:
   print(f"MUTE")
else:
   print(f"TWEET")
