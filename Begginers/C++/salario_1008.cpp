#include <stdio.h>
 
int main() {
 
    int a, b, number;
    double c, salary;
    
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%lf", &c);
    
    salary = b * c;
    
    printf("NUMBER = %d\n", a);
    printf("SALARY = U$ %.2lf\n", salary);
 
    return 0;
}
