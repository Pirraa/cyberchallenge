#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

// Function to check if there exists any triplet in the range [l, r] such that a_i * a_j = a_k^2
bool has_valid_triplet(const vector<int>& sequence, int l, int r) {
    // We'll check all triplets (i, j, k) within this range
    for (int i = l; i <= r; ++i) {
        for (int j = l; j <= r; ++j) {
            for (int k = l; k <= r; ++k) {
                if (i != j && j != k && i != k) {
                    int a = sequence[i];
                    int b = sequence[j];
                    int c = sequence[k];
                    if (a * b == c * c) {
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

// Function to count the number of valid pairs (l, r)
int count_valid_pairs(const vector<int>& sequence, int N) {
    int count = 0;
    // Consider all subarrays [l, r]
    for (int l = 0; l < N; ++l) {
        for (int r = l + 1; r < N; ++r) {
            // Check if there's any valid triplet in the subarray [l, r]
            if (has_valid_triplet(sequence, l, r)) {
                ++count;
            }
        }
    }
    return count;
}

int main() {
    freopen("input.txt", "r", stdin); // DECOMMENT IF YOU WANT TO READ FROM FILE
    freopen("output1.txt", "w", stdout); // DECOMMENT IF YOU WANT TO WRITE TO FILE
    int T;
    cin >> T; // Number of test cases

    // For each test case
    for (int t = 0; t < T; ++t) {
        int N;
        cin >> N; // Length of the sequence
        vector<int> sequence(N);
        
        // Read the sequence
        for (int i = 0; i < N; ++i) {
            cin >> sequence[i];
        }

        // Output the result for this test case
        cout << count_valid_pairs(sequence, N) << endl;
    }

    return 0;
}
