#include <stdio.h>
 
int main() {
 
    int km;
    double combustivel;
    
    scanf("%d", &km);
    scanf("%lf", &combustivel);
    
    printf("%.3lf km/l\n", km / combustivel);
    
 
    return 0;
}
