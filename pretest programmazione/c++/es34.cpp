#include <iostream>
#include <vector>

int main() {
    int N;
    std::cout << "Enter the value of N: ";
    std::cin >> N;

    std::vector<int> A(N), B(N);

    std::cout << "Enter elements of vector A: ";
    for (int i = 0; i < N; ++i) {
        std::cin >> A[i];
    }

    std::cout << "Enter elements of vector B: ";
    for (int i = 0; i < N; ++i) {
        std::cin >> B[i];
    }

    for (int i = 0; i < N; i += 2) {
        int temp = A[i];
        A[i] = B[i];
        B[i] = temp;
    }

    std::cout << "Vector A after swapping: ";
    for (int i = 0; i < N; ++i) {
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "Vector B after swapping: ";
    for (int i = 0; i < N; ++i) {
        std::cout << B[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}