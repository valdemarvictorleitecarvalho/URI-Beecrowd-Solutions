vertebra = input()
genero = input()
alimento = input()

if vertebra == "vertebrado" and genero == "ave":
   if alimento == "carnivoro":
      print(f"aguia")
   elif alimento == "onivoro":
      print(f"pomba")

if vertebra == "vertebrado" and genero == "mamifero":
   if alimento == "onivoro":
      print(f"homem")
   elif alimento == "herbivoro":
      print(f"vaca")

if vertebra == "invertebrado" and genero == "inseto":
   if alimento == "hematofago":
      print(f"pulga")
   elif alimento == "herbivoro":
      print(f"lagarta")
      
if vertebra == "invertebrado" and genero == "anelideo":
   if alimento == "hematofago":
      print(f"sanguessuga")
   elif alimento == "onivoro":
      print(f"minhoca")