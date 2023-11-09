def conversor(num):
    equivalente = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    valor = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    num_romano = ""
    i = 0
    while  num > 0:
        for k in range(num // valor[i]):
            num_romano += equivalente[i]
            num -= valor[i]
        i += 1
    
    return num_romano

num = int(input())
num_romano = conversor(num)
print(num_romano)
