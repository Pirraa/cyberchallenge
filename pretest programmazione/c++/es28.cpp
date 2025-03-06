#include <iostream>
using namespace std;

void rotateRight(int A[], int N) {
    if (N <= 1) return; // Nessuna rotazione necessaria se il vettore ha 0 o 1 elemento

    int last = A[N - 1]; // Salva l'ultimo elemento

    // Spostiamo gli elementi verso destra
    for (int i = N - 1; i > 0; i--) {
        A[i] = A[i - 1];
    }

    A[0] = last; // L'ultimo elemento va in prima posizione
}

int main() {
    int A[] = {1, 1000, 2, 3, 4};
    int N = sizeof(A) / sizeof(A[0]);

    rotateRight(A, N);

    // Stampa il vettore ruotato
    for (int i = 0; i < N; i++) {
        cout << A[i] << " ";
    }

    return 0;
}
