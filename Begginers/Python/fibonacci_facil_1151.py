N = int(input())

fibonacci = [0,1]

while len(fibonacci) < N:
      fibonacci.append(fibonacci[-1] + fibonacci[-2])
      
for c in range(N):
    if c == N - 1:
       print(fibonacci[c], end="\n")
    else:
       print(fibonacci[c], end=" ")
