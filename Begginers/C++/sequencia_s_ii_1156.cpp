#include <stdio.h>
 
int main() {
    
    int D;
    double S, I;
    
    S = 1.0;
    I = 3.0;
    D = 2.0;
    
    while (I <= 39) {
        S = S + I / D;
        I += 2;
        D *= 2;
    }
    
    printf("%.2f\n", S);
 
    return 0;
}
