vetor_reverso = []

for i in range(20):
    N = int(input())
    vetor_reverso.append(N)

vetor_reverso = vetor_reverso[::-1]

for num, valor in enumerate(vetor_reverso):
    print(f"N[{num}] = {valor}")
