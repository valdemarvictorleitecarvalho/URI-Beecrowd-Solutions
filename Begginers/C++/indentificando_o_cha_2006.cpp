#include <stdio.h>

int main() {
    
    int T, respostas , i, acertou = 0;
            
    scanf("%d", &T);
                    
    for (i = 0; i < 5; i++) {
        scanf("%d", &respostas);
        if (respostas == T) acertou++;
        }
                                                
        printf("%d\n", acertou);
                                                        
        return 0;
}
