#include <iostream>

using namespace std;

int main() {
    const int N = 5; // Dimensione fissa dell'array
    int arr[N];

    // 1. Inserimento dei numeri
    cout << "Inserisci " << N << " numeri interi:" << endl;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    cout << "Elementi ripetuti: ";

    // 2. Ricerca degli elementi ripetuti
    bool trovato = false;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (arr[i] == arr[j]) { 
                // Controllo per evitare di stampare più volte lo stesso numero
                bool giaStampato = false;
                for (int k = 0; k < i; k++) {
                    if (arr[k] == arr[i]) {
                        giaStampato = true;
                        break;
                    }
                }
                if (!giaStampato) {
                    cout << arr[i] << " ";
                    trovato = true;
                }
                break; // Interrompe il ciclo j per evitare stampe multiple
            }
        }
    }

    if (!trovato) {
        cout << "Nessun elemento ripetuto.";
    }
    
    cout << endl;
    return 0;
}
