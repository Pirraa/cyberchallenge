using namespace std;
#include <iostream>
#include <vector> // Necessaria per std::vector
#include <random>

int main() {
    cout << "Ciao, mondo!" << endl;
    // Gestione classica con array
    const int DIM = 5;
    int array[DIM] = {1, 2, 3, 4, 5}; // Array statico di dimensione fissa
    int sommaArray = 0;

    // Sommare gli elementi dell'array classico
    for (int i = 0; i < DIM; ++i) {
        sommaArray += array[i];
    }
    std::cout << "Somma degli elementi nell'array classico: " << sommaArray << std::endl;

    // Aggiunta di un elemento (non possibile direttamente, array statico!)
    // Bisogna creare un nuovo array più grande manualmente (non mostrato qui per semplicità).

    // Gestione con std::vector
    std::vector<int> vettore = {1, 2, 3, 4, 5}; // Vettore dinamico
    int sommaVettore = 0;

    // Aggiungere un elemento al vettore
    vettore.push_back(6); // Aggiunge il numero 6 al vettore

    // Sommare gli elementi del vettore
    for (int numero : vettore) {
        sommaVettore += numero;
    }
    std::cout << "Somma degli elementi nel vettore: " << sommaVettore << std::endl;

    // Rimuovere l'ultimo elemento
    vettore.pop_back();
    // Stampare gli elementi del vettore
    std::cout << "Elementi del vettore: ";
    for (int numero : vettore) {
        std::cout << numero << " ";
    }
    std::cout << std::endl;


    // Creare una fonte di entropia hardware
    std::random_device rd; 

    // Inizializzare il Mersenne Twister con un seed generato dall'entropia hardware
    std::mt19937 gen(rd());

    // Definire una distribuzione uniforme
    std::uniform_int_distribution<> distribuzione(1, 100);

    // Generare e stampare numeri casuali
    for (int i = 0; i < 10; ++i) {
        std::cout << distribuzione(gen) << " ";
    }
    std::cout << std::endl;


    std::srand(std::time(nullptr)); // Imposta un seed basato sull'orologio

    // Genera e stampa 10 numeri casuali tra 1 e 100
    for (int i = 0; i < 10; ++i) {
        int numeroCasuale = std::rand() % 100 + 1; // Intervallo [1, 100]
        std::cout << numeroCasuale << " ";
    }
    std::cout << std::endl;

    return 0;
}
