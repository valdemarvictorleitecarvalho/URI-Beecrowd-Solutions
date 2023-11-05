repeticoes = int(input())
string = "Feliz natal!"
nova_string = ""

for j in range(8):
    nova_string += string[j]

for i in range(8, len(string)):
    nova_string += string[i]
            
    if string[i] == "a":
       for adicionais in range(repeticoes - 1):
           nova_string += "a"
                                             
print(nova_string)
