disponiveis = [int(x) for x in input().split()]
dis_frango = disponiveis[0]
dis_bife = disponiveis[1]
dis_massa = disponiveis[2]

requisitados = [int(x) for x in input().split()]
req_frango = requisitados[0]
req_bife = requisitados[1]
req_massa = requisitados[2]

faltou = 0

if dis_frango < req_frango:
   faltou += req_frango - dis_frango
if dis_bife < req_bife:
   faltou += req_bife - dis_bife
if dis_massa < req_massa:
   faltou += req_massa - dis_massa
   
print(faltou)
