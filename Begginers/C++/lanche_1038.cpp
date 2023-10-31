#include <stdio.h>
 
int main() {
 
    int codint, qtint;
    double qtdouble, preco;
    
    scanf("%d %d", &codint, &qtint);
    
    qtdouble = (double)qtint;
    
    if (codint == 1) {
        preco = 4.00;
    }
    else if (codint == 2) {
        preco = 4.50;
    }
    else if (codint == 3) {
        preco = 5.00;
    }
    else if (codint == 4) {
        preco = 2.00;
    }
    else if (codint == 5) {
        preco = 1.50;
    }
    
    printf("Total: R$ %.2lf\n", qtdouble * preco);
    
    return 0;
}
