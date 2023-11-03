#include <iostream>

int main() {
    int entrada;
    scanf("%d", &entrada);

    for (int j = 0; j < entrada; j++) {
        int N;
        scanf("%d", &N);
        bool ehPrimo = true;

        if (N <= 1) {
            ehPrimo = false;
        } else {
            for (int i = 2; i * i <= N; i++) {
                if (N % i == 0) {
                    ehPrimo = false;
                    break;
                }
            }
        }

        if (ehPrimo) {
            printf("%d eh primo\n", N);
        } else {
            printf("%d nao eh primo\n", N);
        }
    }

    return 0;
}
