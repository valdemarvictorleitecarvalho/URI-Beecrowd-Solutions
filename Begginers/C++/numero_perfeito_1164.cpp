#include <iostream>

int main() {
    int entrada;
    
    scanf("%d", &entrada);

    for (int j = 0; j < entrada; j++) {
        int N;
        scanf("%d", &N);
        int soma = 0;

        for (int i = 1; i < N; i++) {
            if (N % i == 0) {
                soma += i;
            }
        }

        if (soma == N) {
            printf("%d eh perfeito\n", N);
        } else {
            printf("%d nao eh perfeito\n", N);
        }
    }

    return 0;
}
