#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> vetor_reverso;

    for (int i = 0; i < 20; i++) {
        int N;
        scanf("%d", &N);
        vetor_reverso.push_back(N);
    }

    std::reverse(vetor_reverso.begin(), vetor_reverso.end());

    for (int num = 0; num < 20; num++) {
        int valor = vetor_reverso[num];
        printf("N[%d] = %d\n", num, valor);
    }

    return 0;
}
