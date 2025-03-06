#include <iostream>

using namespace std;

int main() {
    int N;
    
    // Richiedere la dimensione del vettore
    cout << "Inserisci la dimensione del vettore A: ";
    cin >> N;

    int* A = new int[N]; // Vettore A
    int* B = new int[N - 1]; // Vettore B avrà dimensione N-1

    // Inserimento degli elementi in A
    cout << "Inserisci " << N << " numeri interi per il vettore A:" << endl;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    // Creazione del vettore B
    for (int i = 0; i < N - 1; i++) {
        B[i] = A[i] * A[i + 1]; // Prodotto degli elementi adiacenti
    }

    // Stampa del vettore B
    cout << "Vettore B: ";
    for (int i = 0; i < N - 1; i++) {
        cout << B[i] << " ";
    }
    cout << endl;

    delete[] B; // Deallocazione della memoria
    delete[] A; // Deallocazione della memoria per A
    return 0;
}
