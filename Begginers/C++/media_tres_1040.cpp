#include <stdio.h>
 
int main() {
 
    double n1, n2, n3, n4, media, notaexame, mediaf;
    
    scanf("%lf %lf %lf %lf", &n1, &n2, &n3, &n4);
    
    media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10.0;
    
    printf("Media: %.1lf\n", media);
    
    if (media >= 7) {
        printf("Aluno aprovado.\n");
    }
    else if (media < 5) {
        printf("Aluno reprovado.\n");
    }
    else if (media >= 5 && media <= 6.9) {
        printf("Aluno em exame.\n");
        
        scanf("%lf", &notaexame);
        
        mediaf = (notaexame + media) / 2.0;
        
        printf("Nota do exame: %.1lf\n", notaexame);
        
        if (mediaf >= 5) {
            printf("Aluno aprovado.\n");
            printf("Media final: %.1lf\n", mediaf);
        }
        else {
            printf("Aluno reprovado.\n");
            printf("Media final: %.1lf\n", mediaf);
        }
    }
    
    return 0;
}
