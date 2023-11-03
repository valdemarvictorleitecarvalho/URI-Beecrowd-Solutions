#include <cstdio>
#include <vector>

int main() {
    int T;
    scanf("%d", &T);

    int i = 0;
    std::vector<int> resposta;

    while (i < T) {
        int R1, R2;
        scanf("%d %d", &R1, &R2);
        resposta.push_back(R1 + R2);
        i++;
    }

    for (int j = 0; j < resposta.size(); j++) {
        printf("%d\n", resposta[j]);
    }

    return 0;
}
