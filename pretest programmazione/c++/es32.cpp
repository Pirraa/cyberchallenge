#include <iostream>
#include <vector>
using namespace std;

vector<int> mergeAlternating(const vector<int>& A, const vector<int>& B) {
    vector<int> C;
    int i = 0, j = B.size() - 1; // i parte dall'inizio di A, j parte dalla fine di B
    int sizeA = A.size(), sizeB = B.size();

    while (i < sizeA || j >= 0) {
        if (i < sizeA) {
            C.push_back(A[i]);
            i++;
        }
        if (j >= 0) {
            C.push_back(B[j]);
            j--;
        }
    }
    return C;
}

int main() {
    // Test con vettori di stessa dimensione
    vector<int> A = {1, 2, 3, 4};
    vector<int> B = {10, 20, 30, 40};

    // Test con vettori di dimensione diversa
    // vector<int> A = {1, 2, 3, 4, 5};  
    // vector<int> B = {10, 20, 30};

    vector<int> C = mergeAlternating(A, B);

    // Stampa il vettore risultante
    cout << "Vettore C: { ";
    for (int num : C) cout << num << " ";
    cout << "}" << endl;

    return 0;
}
