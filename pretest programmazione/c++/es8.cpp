#include <iostream>

using namespace std;

int main() {
    int N;
    
    // Richiedere la dimensione del vettore
    cout << "Inserisci la dimensione massima del vettore N: ";
    cin >> N;

    int* V = new int[N]; // Vettore di dimensione N
    int count = 0; // Contatore degli elementi inseriti

    while (true) {
        int num;
        cout << "Inserisci un numero (0 per terminare): ";
        cin >> num;

        if (num == 0) {
            break; // Termina il programma se l'utente inserisce 0
        }

        if (count < N) {
            // Se il vettore non è pieno, aggiungi il valore normalmente
            V[count] = num;
            count++;
        } else {
            // Se il vettore è pieno, scorrere gli elementi e aggiungere in fondo
            for (int i = 0; i < N - 1; i++) {
                V[i] = V[i + 1]; // Shift a sinistra
            }
            V[N - 1] = num; // Inserisce il nuovo valore in fondo
        }

        // Stampa del vettore aggiornato
        cout << "Vettore attuale: ";
        for (int i = 0; i < count; i++) {
            cout << V[i] << " ";
        }
        cout << endl;
    }

    cout << "Programma terminato!" << endl;
    delete[] V; // Libera la memoria allocata dinamicamente
    return 0;
}
