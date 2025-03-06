#include <stdio.h>
#include <limits.h> // Per INT_MIN

int trovaMassimo(int A[], int N) {
    int massimo = INT_MIN;
    int indiceMassimo = -1;

    for (int i = 0; i < N; i++) {
        if (A[i] > massimo) {
            massimo = A[i];
            indiceMassimo = i;
        }
    }

    return indiceMassimo;
}

void ordinaDecrescente(int A[], int B[], int N) {
    for (int i = 0; i < N; i++) {
        int indiceMassimo = trovaMassimo(A, N); // Trova l'indice del massimo
        B[i] = A[indiceMassimo]; // Copia il massimo in B
        A[indiceMassimo] = INT_MIN; // "Rimuovi" il massimo da A
    }
}

int main() {
    int A[] = {3, 1, 4, 1, 5, 9, 2, 6, 5};
    int B[] = {0,0,0,0,0,0,0,0,0};

    for (int i = 0; i < 9; i++) 
    {
        int massimo = INT_MIN;
        int indiceMassimo = -1;

        for (int i = 0; i < 9; i++) 
        {
            if (A[i] > massimo) 
            {
                massimo = A[i];
                indiceMassimo = i;
            }
        }
        B[i] = A[indiceMassimo]; // Copia il massimo in B
        A[indiceMassimo] = INT_MIN; // "Rimuovi" il massimo da A
    }

    // Stampa il vettore ordinato B
    printf("Vettore ordinato in ordine decrescente:\n");
    for (int i = 0; i < 9; i++) {
        printf("%d ", B[i]);
    }
    printf("\n");

    return 0;
}