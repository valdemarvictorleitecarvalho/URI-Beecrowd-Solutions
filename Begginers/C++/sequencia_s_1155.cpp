#include <stdio.h>
 
int main() {
 
    int i;
    double S; 
    
    S = 0;
    
    for (int i = 1; i <= 100; i++) {
        S += 1.0/i;
    }
    
    printf("%.2f\n", S);
    
    return 0;
}
