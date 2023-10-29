#include <stdio.h>
 
int main() {
 
    double raio, pi;
    pi = 3.14159;
    
    scanf("%lf", &raio);
    printf("A=%.4lf\n", raio*raio*pi);
    
    return 0;
}