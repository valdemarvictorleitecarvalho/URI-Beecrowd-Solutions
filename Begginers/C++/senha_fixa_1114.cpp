#include <stdio.h>
 
int main() {
 
    int senha;

    while(true) {
        scanf("%d", &senha);
        
        if (senha == 2002) {
        printf("Acesso Permitido\n"); 
        break;
    }
    else {
        printf("Senha Invalida\n");
    }
    }
    
    return 0;
}
