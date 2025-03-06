#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <array>

using namespace std;

void printVector(const vector<int>& vec) {
    cout << "[";
    for (size_t i = 0; i < vec.size(); ++i) {
        cout << vec[i];
        if (i < vec.size() - 1) cout << ",";
    }
    cout << "]";
}

int find_subsets(int N, int D, vector<int> S){
    // SCRIVI QUA IL TUO CODICE
    //s viene diviso in due gruppi A e B di tutte le possibili dimensioni
    //faccio la differenza fra ogni elemento di A e B con tutti gli altri nello stesso gruppo
    //controllo se la differenza è minore di D
    //se la differenza è minore di d incremento il contatore
    //per tutti i possibili sottogruppi A e B controllo se il contatore è più grande del contatore massimo
    //se è più grande del contatore massimo lo sostituisco e memorizzo la lunghezza di a e di b per poi farne la somma
    int max=0; bool flag=false;
    int limit=(int)ceil((double)N/2);
    for(int i=1; i<N; i++)
    {
            //creo tutti i possibili vettori A e B di dimensione i e j
            vector<int> indices(S.size());
            for (int k = 0; k < S.size(); ++k) {
                indices[k] = k < i ? 1 : 0; // Inizializza per selezionare i elementi
            }

            // Genera tutte le combinazioni
            do 
            {
                flag=true;
                //vettore A avrà dimensione i
                vector<int> A;
                //vettore B avrà dimensione N-i
                vector<int> B;
                for (int k = 0; k < S.size(); ++k) 
                {
                    if (indices[k] == 1) {
                        A.push_back(S[k]); // Elementi scelti per A
                    } else {
                        B.push_back(S[k]); // Elementi rimanenti per B
                    }
                }

                // Stampa i vettori A e B
                cout << "A = ";
                printVector(A);
                cout << ", B = ";
                printVector(B);
                cout << endl;

                //controllo tutte le possibili differenze di a
                for(int k=0; k<A.size(); k++){
                    for(int l=k+1; l<A.size(); l++){
                        if(k!=l){
                            if(abs(A[k]-A[l])>D){
                                //cout << "true: " << A[k] << " - " << A[l] << " = " << abs(A[k]-A[l]) << endl;
                                flag=false;
                                break;
                            }
                        }
                    }
                }
                //controllo tutte le possibili differenze di b
                for(int k=0; k<B.size(); k++){
                    for(int l=k+1; l<B.size(); l++){
                        if(k!=l){
                            if(abs(B[k]-B[l])>D){
                                flag=false;
                                break;
                            }
                        }
                    }
                }
                //cout << A.size() << " " << B.size() << endl;
                cout << "flag: " << flag << endl;
                //controllo se il contatore di a e b è maggiore del massimo
                if(flag==true && A.size()+B.size()>max){
                    max=A.size()+B.size();
                    cout << "max: " << max << " lena: " << A.size() << " lenb: " << B.size() << endl;
                }

            } while (prev_permutation(indices.begin(), indices.end()));
    }
    return max;
}

int main(){

    freopen("input2.txt", "r", stdin); // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
    freopen("output.txt", "w", stdout); // DECOMMENTA QUA SE VUOI SCRIVERE DA FILE
    int T;
    cin >> T;

    while(T--){
        int N, D;
        vector<int> S;

        cin >> N >> D;
        
        for(int i = 0; i < N; i++){
            int x;
            cin >> x;
            S.push_back(x);
        }
        
        cout << find_subsets(N, D, S) << endl;
    }

    return 0;
}