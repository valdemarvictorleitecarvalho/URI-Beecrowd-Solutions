#include <stdio.h>

int main() {
 
    int valor, total, i;
    
    while (1) {
        scanf("%d", &valor);
        
        if (valor == 0) {
            break;
        }

        total = 0; 

        if (valor % 2 == 0) {
            for (i = valor; i <= valor + 9; i += 2) {
                total += i;
            }
        }
        else {
            for (i = valor + 1; i <= valor + 10; i += 2) {
                total += i;
            }
        }
        
        printf("%d\n", total);
    }
 
    return 0;
}
