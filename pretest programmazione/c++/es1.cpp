#include <iostream>

using namespace std;

int main() {
    int N;

    // 1. Chiedere il numero N
    cout << "Inserisci la dimensione del vettore: ";
    cin >> N;

    //int arr[N];

    // Allocazione dinamica dell'array
    int* arr = new int[N];

    // 2. Riempire l'array con N numeri
    cout << "Inserisci " << N << " numeri:" << endl;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    // 3. Chiedere il numero NUM da cercare
    int NUM;
    cout << "Inserisci il numero da cercare: ";
    cin >> NUM;

    // 4. Cercare NUM nel vettore e stampare la prima posizione trovata
    bool trovato = false;
    for (int i = 0; i < N; i++) {
        if (arr[i] == NUM) {
            cout << "Numero trovato alla posizione: " << i << endl;
            trovato = true;
            break;
        }
    }

    if (!trovato) {
        cout << "Numero non presente nel vettore." << endl;
    }

    // Deallocazione della memoria
    delete[] arr;

    return 0;
}
