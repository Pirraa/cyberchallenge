#include <iostream>
#include <vector>
using namespace std;

vector<int> sommaCoppie(const vector<int>& A) {
    vector<int> B;
    int N = A.size();

    for (int i = 0; i < N - 1; i += 2) {  // Somma coppie di elementi
        B.push_back(A[i] + A[i + 1]);
    }

    if (N % 2 != 0) {  // Se A ha un numero dispari di elementi, aggiungiamo l'ultimo elemento
        B.push_back(A[N - 1]);
    }

    return B;
}

void stampaVettore(const vector<int>& V) {
    cout << "{ ";
    for (int num : V) cout << num << " ";
    cout << "}" << endl;
}

int main() {
    vector<int> A1 = {5,1,1,2};
    vector<int> A2 = {5,1,1,2,7};

    vector<int> B1 = sommaCoppie(A1);
    vector<int> B2 = sommaCoppie(A2);

    cout << "A1 = {5,1,1,2} -> B1 = ";
    stampaVettore(B1);

    cout << "A2 = {5,1,1,2,7} -> B2 = ";
    stampaVettore(B2);

    return 0;
}
