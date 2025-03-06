#include <iostream>
#include <cstring> // Per funzioni sulle stringhe in stile C
#include <string>  // Per std::getline
using namespace std;

int main() {
    char stringa[] = "Ciao, mondo!"; // Inizializzazione diretta con una stringa
    cout << "Stringa: " << stringa << endl;

    // Modifica di un carattere
    stringa[5] = 'M';
    cout << "Dopo modifica: " << stringa << endl;

    // Lunghezza della stringa
    cout << "Lunghezza: " << strlen(stringa) << endl;

    string stringa2 = "Ciao, mondo!"; // Dichiarazione di una stringa
    cout << "Stringa: " << stringa << endl;

    // Modifica della stringa
    stringa2 += " Come stai?"; // Aggiunta di testo
    cout << "Dopo aggiunta: " << stringa << endl;

    // Lunghezza della stringa
    cout << "Lunghezza: " << stringa2.length() << endl;

    // Accesso ai caratteri
    cout << "Primo carattere: " << stringa2[0] << endl;

    string s1 = "Ciao";
    string s2 = " mondo!";
    string risultato = s1 + s2; // "Ciao mondo!"

    cout << s1.length(); // Ritorna la lunghezza di s1

    if (s1 == s2) {
        cout << "Le stringhe sono uguali.";
    }

    string sotto = s1.substr(0, 2); // Prende i primi 2 caratteri

    size_t posizione = s1.find("ao"); // Ritorna l'indice del primo match

    string nome;

    cout << "Inserisci il tuo nome: ";
    std::getline(cin, nome); // Legge una riga completa, incluso lo spazio

    cout << "Ciao, " << nome << "! Benvenuto in C++." << endl;


    return 0;
}
