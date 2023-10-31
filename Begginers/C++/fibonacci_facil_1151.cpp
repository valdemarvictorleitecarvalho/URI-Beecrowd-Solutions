#include <iostream>
#include <vector> 

int main() {
    int N;
    std::vector<int> fib = {0, 1}; 
    
    scanf("%d", &N);
    
    while (fib.size() < N) {
        int next = fib[fib.size() - 1] + fib[fib.size() - 2];
        fib.push_back(next);
    }
    
    for (int c = 0; c < N; c++) {
        if (c == N - 1) {
            printf("%d\n", fib[c]);
        } else {
            printf("%d ", fib[c]);
        }
    }
    
    return 0;
}
