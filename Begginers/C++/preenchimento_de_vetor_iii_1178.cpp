#include <iostream>

int main() {
    
    int i;
    double X;
    
    scanf("%lf", &X);
    
    for (i = 0; i <= 99; i++) {
        printf("N[%d] = %.4lf\n", i, X);
        X = X / 2.0;
    }

    return 0;
}
