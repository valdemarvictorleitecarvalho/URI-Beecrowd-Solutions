#include <stdio.h>
 
int main() {
 
    int x, i, maior, n, contador;
    
    maior = 0;
    
    for (int i = 1; i <= 100; i++) {
        scanf("%d", &x);
        if (x > maior) {
            maior = x;
            contador = i;
        }
        
    }
    
    printf("%d\n%d\n",maior, contador);
 
    return 0;
}
