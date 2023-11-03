substituicoes = {
    '*': '1',
    '-': '0'
}

grito = 0
soma = 0

while True:
    entrada = input()

    if entrada == "caw caw":
        grito += 1
        print(soma)
        soma = 0
    else:
         entrada_modificada = ''.join([substituicoes.get(c, c) for c in entrada])

         decimal_output = int(entrada_modificada, 2)
    
         soma += decimal_output
    
    if grito >= 3:
        break
