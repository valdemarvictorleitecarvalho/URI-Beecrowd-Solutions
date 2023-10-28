n = int(input())

i = 0
o = 0
 
for c in range(n):
    x = int(input())
    if 10 <= x <= 20:
       i += 1
    else:
       o +=1

print(f"{i} in")
print(f"{o} out")