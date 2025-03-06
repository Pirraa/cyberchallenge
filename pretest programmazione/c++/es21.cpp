#include <iostream>

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

void unionArrays(int A[], int sizeA, int B[], int sizeB, int C[], int &sizeC) {
    sizeC = 0;
    for (int i = 0; i < sizeA; i++) {
        C[sizeC++] = A[i];
    }
    for (int i = 0; i < sizeB; i++) {
        bool found = false;
        for (int j = 0; j < sizeA; j++) {
            if (B[i] == A[j]) {
                found = true;
                break;
            }
        }
        if (!found) {
            C[sizeC++] = B[i];
        }
    }
}

void intersectionArrays(int A[], int sizeA, int B[], int sizeB, int C[], int &sizeC) {
    sizeC = 0;
    for (int i = 0; i < sizeA; i++) {
        for (int j = 0; j < sizeB; j++) {
            if (A[i] == B[j]) {
                C[sizeC++] = A[i];
                break;
            }
        }
    }
}

void differenceArrays(int A[], int sizeA, int B[], int sizeB, int C[], int &sizeC) {
    sizeC = 0;
    for (int i = 0; i < sizeA; i++) {
        bool found = false;
        for (int j = 0; j < sizeB; j++) {
            if (A[i] == B[j]) {
                found = true;
                break;
            }
        }
        if (!found) {
            C[sizeC++] = A[i];
        }
    }
}

int main() {
    int A[] = {1, 2, 3, 4, 5};
    int B[] = {4, 5, 6, 7, 8};
    int sizeA = sizeof(A) / sizeof(A[0]);
    int sizeB = sizeof(B) / sizeof(B[0]);
    int C[10];
    int sizeC;

    // Union
    unionArrays(A, sizeA, B, sizeB, C, sizeC);
    std::cout << "Union: ";
    printArray(C, sizeC);

    // Intersection
    intersectionArrays(A, sizeA, B, sizeB, C, sizeC);
    std::cout << "Intersection: ";
    printArray(C, sizeC);

    // Difference
    differenceArrays(A, sizeA, B, sizeB, C, sizeC);
    std::cout << "Difference: ";
    printArray(C, sizeC);

    return 0;
}