#include <iostream>
#include <vector>
using namespace std;

int main() {
    int righe, colonne;

    // Input delle dimensioni della matrice
    cout << "Inserisci il numero di righe: ";
    cin >> righe;
    cout << "Inserisci il numero di colonne: ";
    cin >> colonne;

    // Creazione della matrice come vector di vector
    vector<vector<int>> matrice(righe, vector<int>(colonne));

    // Inizializzazione degli elementi
    cout << "Inserisci gli elementi della matrice:" << endl;
    for (int i = 0; i < righe; i++) {
        for (int j = 0; j < colonne; j++) {
            cout << "Elemento [" << i << "][" << j << "]: ";
            cin >> matrice[i][j];
        }
    }

    // Stampa della matrice
    cout << "\nMatrice inserita:" << endl;
    for (int i = 0; i < righe; i++) {
        for (int j = 0; j < colonne; j++) {
            cout << matrice[i][j] << " ";
        }
        cout << endl;
    }




    int righe, colonne;

    // Input delle dimensioni della matrice
    cout << "Inserisci il numero di righe: ";
    cin >> righe;
    cout << "Inserisci il numero di colonne: ";
    cin >> colonne;

    // Allocazione dinamica della matrice
    int** matrice2 = new int * [righe];
    for (int i = 0; i < righe; i++) {
        matrice2[i] = new int[colonne];
    }

    // Inizializzazione degli elementi
    cout << "Inserisci gli elementi della matrice:" << endl;
    for (int i = 0; i < righe; i++) {
        for (int j = 0; j < colonne; j++) {
            cout << "Elemento [" << i << "][" << j << "]: ";
            cin >> matrice2[i][j];
        }
    }

    // Stampa della matrice
    cout << "\nMatrice inserita:" << endl;
    for (int i = 0; i < righe; i++) {
        for (int j = 0; j < colonne; j++) {
            cout << matrice2[i][j] << " ";
        }
        cout << endl;
    }

    // Deallocazione della memoria
    for (int i = 0; i < righe; i++) {
        delete[] matrice2[i];
    }
    delete[] matrice2;

    return 0;
}
