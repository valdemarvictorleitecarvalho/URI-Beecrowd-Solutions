compras = int(input())
valor = 0

while compras != 0:
      compra = input().split()
      pedido = compra[0]
      quantia = int(compra[1])
                        
      if pedido == "1001":
         valor += 1.50 * quantia
      elif pedido == "1002":
         valor += 2.50 * quantia
      elif pedido == "1003":
         valor += 3.50 * quantia
      elif pedido == "1004":
         valor += 4.50 * quantia
      elif pedido == "1005":
         valor += 5.50 * quantia
                                                                                                                      
      compras -= 1
                                                                                                                                  
print(f"{valor:.2f}")
