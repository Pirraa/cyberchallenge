using namespace std;
#include <iostream>
#include <vector> // Necessaria per std::vector
#include <random>

int controlloCelle(vector<string> matrice,int i,int j,int M,int N)
{
    int counter=0;
    for(int k=i-1;k<=i+1;k++)
    {
        for(int l=j-1;l<=j+1;l++)
        {
            if(k>=0 && k<N && l>=0 && l<M && (k!=i || l!=j))
            {
                if(matrice[k][l]=='*' || matrice[k][l]=='+')
                {
                    counter++;
                }
            }
        }
    }
    cout << "Counter: " << counter << endl;
    return counter;
}

int main()
{
    int M,N,K;
    cin >> N >> M >> K;
    // Allocazione dinamica della matrice
    /*char** matrice = new char*[N];
    for (int i = 0; i < N; i++) {
        matrice[i] = new char[M];
    }*/
    vector<string> matrice(N, string(M, '.'));

    // Inizializzazione della matrice
    for(int i = 0; i < N; i++) {
        //cout << "Inserisci la \'" << i << "\' riga della matrice" << endl;
        for(int j = 0; j < M; j++) {
            cin >> matrice[i][j];
        }
    }

    for(int k=0; k<K;k++)
    {
        vector<string> matrice2(N, string(M, '.'));
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
            {
                int count=controlloCelle(matrice,i,j,M,N);


                matrice2[i][j] = matrice[i][j];

                if(matrice[i][j]=='.' && count> 4)
                {
                    matrice2[i][j]='+';
                }

                else if(matrice[i][j]=='+')
                {
                    if(count>4)
                        matrice2[i][j]='*';
                    if(count <4)
                        matrice2[i][j]='.';
                }
                
                //if(matrice[i][j]=='*' )
                else
                {
                    if(count<4)
                        matrice2[i][j]='.';
                    if(count>4)
                        matrice2[i][j]='+';
                }
                
                
                
            }
        matrice=matrice2;  
    }

    //Stampa della matrice
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cout << matrice[i][j] << " ";
        }
        cout << endl;
    }

    
}

