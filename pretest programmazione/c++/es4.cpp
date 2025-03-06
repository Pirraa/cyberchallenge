#include <iostream>

using namespace std;

int main() {
    const int N = 10; // Dimensione dei vettori
    int A[N] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int B[N] = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19};

    // Scambio dei primi 5 elementi di A con gli ultimi 5 di B
    for (int i = 0; i < 5; i++) {
        swap(A[i], B[i + 5]);
    }

    // Scambio degli ultimi 5 elementi di A con i primi 5 di B
    for (int i = 5; i < 10; i++) {
        swap(A[i], B[i - 5]);
    }

    // Scambio inverso degli elementi tra A e B
    for (int i = 0; i < N; i++) {
        swap(A[N - 1 - i], B[i]);
    }

    // Stampa dei risultati
    cout << "Vettore A dopo lo scambio: ";
    for (int i = 0; i < N; i++) {
        cout << A[i] << " ";
    }
    cout << endl;

    cout << "Vettore B dopo lo scambio: ";
    for (int i = 0; i < N; i++) {
        cout << B[i] << " ";
    }
    cout << endl;

    return 0;
}
