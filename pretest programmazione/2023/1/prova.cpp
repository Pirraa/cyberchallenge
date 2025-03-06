using namespace std;
#include <iostream>
#include <vector> // Necessaria per std::vector
#include <random>

int main()
{
    int Q,N;
    cout << "Inserisci il numero di domande: ";
    cin >> Q;
    cout << "Inserisci il numero di utenti: ";
    cin >> N;

    string corrette(Q, ' ');

    cout << "Inserisci risposte corrette: ";
    cin >> corrette;

    vector<string> utenti(N);

    cout << "Inserisci risposte utenti: ";
    for(int i=0; i<N;i++){
        cin >> utenti[i];
    }

    vector <int> punteggi(N,0);

   
    for(int i=0;i<Q;i++)
    {
        for(int j=0;j<N;j++){
            if(corrette[i]==utenti[j][i])
            {
                punteggi[j]++;
            }
        }
    }

    for(int i=0;i<N;i++){
        cout << punteggi[i] << endl;
    }
}