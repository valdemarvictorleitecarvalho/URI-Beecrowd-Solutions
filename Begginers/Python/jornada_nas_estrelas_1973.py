N = int(input())
cordeiro = list(map(int, input().split()))
estrelas = [0] * N
soma_estrelas = 0
soma_cordeiro = 0

i = 0

while True:
    modulo = cordeiro[i] % 2
    if i == 0 and modulo == 0:
       estrelas[i] = 1
       if cordeiro[i] > 0:
          cordeiro[i] -= 1
       break
    elif i == N - 1 and modulo == 1:
       estrelas[i] = 1
       if cordeiro[i] > 0:
          cordeiro[i] -= 1
       break
    elif modulo == 1:
       cordeiro[i] -= 1
       estrelas[i] = 1
       i += 1
    elif modulo == 0:
       estrelas[i] = 1
       if cordeiro[i] > 0:
          cordeiro[i] -= 1
       i -= 1

print(estrelas.count(1), sum(cordeiro))
