#include <iostream>

int main() {
    
    int X, Y, A, C;
    
    A = 1;
    
    scanf("%d %d", &X, &Y);
    
    for (int C = 1; C < Y + 1; C++) {
        if (A == X) {
           printf("%d\n", C);
           A = 1;
        }
        else {
            printf("%d ", C);
            A += 1;
        }
    }

    return 0;
}
