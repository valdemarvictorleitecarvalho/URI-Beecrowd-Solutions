#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int N;
    scanf("%d", &N);

    vector<int> X(N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &X[i]);
    }

    int minimum = X[0];
    int result = 1;

    for (int i = 1; i < N; i++) {
        if (X[i] < minimum) {
            minimum = X[i];
            result = i + 1;
        }
    }

    printf("%d\n", result);

    return 0;
}
