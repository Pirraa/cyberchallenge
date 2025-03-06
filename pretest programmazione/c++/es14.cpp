#include <stdio.h>

int main() {
    int A[] = {0, 0, 0, 0, 56, 0, 0, 0, 0, 71};
    int N = sizeof(A) / sizeof(A[0]);

    for (int i = 0; i < N; i++) {
        if (A[i] == 0) {
            for (int j = i + 1; j < N; j++) {
                if (A[j] != 0) {
                    // Scambia A[i] e A[j]
                    int temp = A[i];
                    A[i] = A[j];
                    A[j] = temp;
                    break; // Esci dal ciclo interno dopo lo scambio
                }
            }
        }
    }

    // Stampa il vettore risultante
    for (int i = 0; i < N; i++) {
        printf("%d ", A[i]);
    }

    return 0;
}