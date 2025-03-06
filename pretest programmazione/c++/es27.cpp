#include <iostream>
using namespace std;

void shift(int A[], int N) {
    int maxIndex = 0;
    for (int i = 1; i < N; i++) {
        if (A[i] > A[maxIndex]) {
            maxIndex = i;
        }
    }

    if (maxIndex < N - 1) {  
        for (int i = maxIndex; i < N - 1; i++) {
            A[i] = A[i + 1]; // Sposta gli elementi indietro
        }
    }
}

int main() {
    int A[] = {1, 1000, 2, 3, 4};
    int N = sizeof(A) / sizeof(A[0]);

    shift(A, N);

    for (int i = 0; i < N; i++) {
        cout << A[i] << " ";
    }
    return 0;
}
