entrada = input().split()
dias = int(entrada[0])
saldo = int(entrada[1])

menor_saldo = saldo

for dia in range(dias):
    movimentacao = int(input())
    if movimentacao > 0:
       saldo += movimentacao
    else:
       saldo -= abs(movimentacao)
    if saldo < menor_saldo:
       menor_saldo = saldo
       
print(menor_saldo)
