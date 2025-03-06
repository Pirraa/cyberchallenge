#include <iostream>
using namespace std;

int main() {
    const int N = 10;
    int A[N], B[N];

    // Input del vettore A
    cout << "Inserisci " << N << " numeri interi per il vettore A: " << endl;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    // Copia i primi 5 elementi in ordine inverso
    for (int i = 0; i < 5; i++) {
        B[i] = A[4 - i];
    }

    // Copia i successivi 5 elementi nell'ordine originale
    for (int i = 5; i < N; i++) {
        B[i] = A[i];
    }

    // Output del vettore B
    cout << "Vettore B: { ";
    for (int i = 0; i < N; i++) {
        cout << B[i] << " ";
    }
    cout << "}" << endl;

    return 0;
}
