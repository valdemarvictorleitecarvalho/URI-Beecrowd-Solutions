#include <iostream>
#include <vector>

int main() {
    int N;
    scanf("%d", &N);
    
    std::vector<int> lista(N);
    for (int i = 0; i < N; i++) {
        int x;
        scanf("%d", &x);
        lista[i] = x;
    }
    
    int menor = lista[0];
    int posicao = 0;
    for (int j = 0; j < N; j++) {
        if (lista[j] < menor) {
            menor = lista[j];
            posicao = j;
        }
    }
    
    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n", posicao);
    
    return 0;
}
