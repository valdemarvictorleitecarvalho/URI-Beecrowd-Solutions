n = int(input())

anos = n // 365
r = n % 365
meses = r // 30
dias = r % 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")