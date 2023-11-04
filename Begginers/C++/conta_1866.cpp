#include <iostream>

int main() {
    int C;
    scanf("%d", &C);
    int contador = 1;

    while (C >= contador) {
          int valor;
          scanf("%d", &valor);

          if (valor % 2 == 0) {
             printf("0\n");
          }
          else {
             printf("1\n");
          }
          contador += 1;                                                                      
          }
         
          return 0;
}
