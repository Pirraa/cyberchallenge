#include <iostream>

bool isSubsequence(int A[], int n, int B[], int m, int &startIndex) {
    for (int i = 0; i <= n - m; ++i) {
        int j = 0;
        while (j < m && A[i + j] == B[j]) {
            ++j;
        }
        if (j == m) {
            startIndex = i;
            return true;
        }
    }
    return false;
}

int main() {
    int A[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int B[] = {4, 5, 6};
    int n = sizeof(A) / sizeof(A[0]);
    int m = sizeof(B) / sizeof(B[0]);
    int startIndex;

    if (isSubsequence(A, n, B, m, startIndex)) {
        std::cout << "La sequenza è presente in A a partire dalla posizione: " << startIndex << std::endl;
    } else {
        std::cout << "La sequenza non è presente in A." << std::endl;
    }

    return 0;
}