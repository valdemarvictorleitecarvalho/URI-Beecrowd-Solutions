#include <iostream>
#include <vector>
#include <sstream>

int main() {
    std::vector<int> reguasint;
    std::string input;
    getline(std::cin, input);
    std::istringstream iss(input);
    int regua;
    
    while (iss >> regua) {
          reguasint.push_back(regua);
          }

    int maximo = reguasint[0];

    for (int i = 0; i < reguasint.size() - 1; i++) {
        int conector = (maximo + reguasint[i + 1]) - 1;
        maximo = conector;
        }

        std::cout << maximo << std::endl;

        return 0;
}
