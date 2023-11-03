#include <stdio.h>
 
int main() {
 
    int i;
    double A;
    
    for (i = 0; i <= 99; i++) {
        scanf("%lf", &A);
        if (A <= 10) {
           printf("A[%d] = %.1f\n", i, A);
        }
    }
 
    return 0;
}
