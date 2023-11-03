#include <cstdio>
#include <string>

std::string slice(const std::string& frase, int x) {
    return frase.substr(0, x);
}

int main() {
    std::string frase = "LIFE IS NOT A PROBLEM TO BE SOLVED";
    int x;
    scanf("%d", &x);

    printf("%s\n", slice(frase, x).c_str());

    return 0;
}
