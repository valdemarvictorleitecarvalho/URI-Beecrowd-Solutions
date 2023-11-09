entrada = input().split()
competidores = int(entrada[0])
qt_folhas = int(entrada[1])
recebe = int(entrada[2])

qt_precisa = recebe * competidores

if qt_folhas >= qt_precisa:
   print(f"S")
else:
   print(f"N")
