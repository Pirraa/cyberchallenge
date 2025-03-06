#include <stdio.h>
#include <iostream>
#include <vector>
#include <array>
#include <map>

using namespace std;

long long count_intervals_err(int N, vector<int> a)
{
    // WRITE YOUR CODE HERE
    //ciclo due volte sull'array a
    //prelevo un array contentente solo gli elementi di a da i a j (indici dei due cicli)
    //controllo se in questo sottoarray c'è una terna tale che a[i]*a[j]==a[k]^2 con i<j<k
    //se c'è registro i e j in una map, il risultato finale è la dimensione della map
    map<int,int> interval_map;
    //codice errato, creando un subarray modifico i riferimenti agli indici i e j originali
    for(int i = 0; i < N; i++)
    {
        for(int j = i+1; j < N; j++)
        {
            vector<int> subarray;
            for(int k = i; k <= j; k++)
            {
                subarray.push_back(a[k]);
            }
            for(int k = 0; k < subarray.size(); k++)
            {
                for(int l = k+1; l < subarray.size(); l++)
                {
                    for(int m = l+1; m < subarray.size(); m++)
                    {
                        if (k != l && l != m && l != k) 
                        {
                            int a = subarray[k];
                            int b = subarray[l];
                            int c = subarray[m];
                            if (a * b == c * c) {
                                interval_map.insert(pair<int,int>(i,j));
                            }
                        }
                    }
                }
            }
        }
    }
    return interval_map.size();
}

int count_intervals(int N, const vector<int>& a) {
    int count = 0;

    // Itera su tutti gli intervalli [i, j]
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            // Cerca triplette valide nell'intervallo [i, j]
            for (int k = i; k <= j; k++) {
                for (int l = i; l <= j; l++) {
                    for (int m = i; m <= j; m++) {
                        if (k != l && l != m && k != m) {
                            int a_k = a[k];
                            int a_l = a[l];
                            int a_m = a[m];
                            if (a_k * a_l == a_m * a_m) {
                                count++;
                                goto next_interval; // Esci dal loop una volta trovato
                            }
                        }
                    }
                }
            }
        next_interval:;
        }
    }
    return count;
}

int main(){
    freopen("input.txt", "r", stdin); // DECOMMENT IF YOU WANT TO READ FROM FILE
    freopen("output1.txt", "w", stdout); // DECOMMENT IF YOU WANT TO WRITE TO FILE

    int T;
    cin >> T;

    while(T--){
        int N;
        cin >> N;
        vector<int> a(N);

        for(auto &x : a) cin >> x;

        cout << count_intervals(N, a) << endl;
    }

    return 0;
}