#include <iostream>
#include <vector>
using namespace std;

bool isPalindrome(const std::vector<int>& vec) {
    int n = vec.size();
    for (int i = 0; i < n / 2; ++i) {
        if (vec[i] != vec[n - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    cout << "Inserisci la dimensione del vettore: ";
    cin >> n;

    vector<int> vec(n);
    cout << "Inserisci gli elementi del vettore: ";
    for (int i = 0; i < n; ++i) {
        cin >> vec[i];
    }

    if (isPalindrome(vec)) {
        cout << "Il vettore è palindromo." << endl;
    } else {
        cout << "Il vettore non è palindromo." << endl;
    }

    return 0;
}