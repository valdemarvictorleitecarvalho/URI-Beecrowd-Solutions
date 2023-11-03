#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int reclamou;

    while (scanf("%d", &reclamou) != EOF) {
        if (reclamou == 0) {
            printf("vai ter copa!\n");
        } else {
            printf("vai ter duas!\n");
        }
    }

    return 0;
}
