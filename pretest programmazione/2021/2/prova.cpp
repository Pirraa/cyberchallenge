#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    int T;
    cout << "Inserisci il numero di test case: ";
    cin >>T;
    for(int i=0; i<T; i++)
    {
        string pwd;
        string hash;
        cout << "Inserisci la password: ";
        cin >> pwd;
        cout << "Inserisci l'hash: ";
        cin >> hash;
        bool found = false;
        int j;
        string nuova;
        
        for(int k=0; k<hash.length(); k++)
        {
            nuova=string(pwd.length(), ' ');
            if(pwd.find(hash[k]) != string::npos)
            {
                nuova[0] = hash[k];
                found = true;
                for(j=1; j<pwd.length() && found==true; j++)
                {
                    if(pwd.find(hash[k+j]) != string::npos)
                    {
                        nuova[j] = hash[k+j];
                    }else
                    {
                        found=false;
                    }
                }
            }
            if(j==pwd.length())
            {
                sort(nuova.begin(), nuova.end());
                sort(pwd.begin(), pwd.end());
                if(nuova != pwd)
                {
                    found = false;
                }else
                {
                    found = true;
                    cout<<found<<endl;
                    break;
                }
            }
            if(k==hash.length()-1)
            {
                cout<<found<<endl;
            }
        }
    /*soluzione ottimizzata:
    ordino p in ordine crescente
    scorro h con due indici i che va da 0 alla lunghezza e j ch va da i+1 alla lunghezza
    faccio una sorto del pezzo che va da i a j e controllo se è uguale a P
    se esegue ritorno true alteimenti vado avanti e se j arriva alla fine ritorno false 

    per ottimizzare faccio due cicli ma nel secondo metto j=+len(p) 
    quindi se arrivo ad avere il pezzo da ordinare minore della lunghezza di p mi fermo

    
    */ 
        
    }
}