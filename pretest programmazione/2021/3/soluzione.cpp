#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    int N, K;
    cin >> N >> K;

    vector<int> V(N);
    for(int i=0; i<N; i++)
    cin >> V[i];

    int solution = 0;

    sort(V.begin(), V.end());
    reverse(V.begin(), V.end());
    for(int i=0; i<K+1; i++) solution += V[i];

    cout << solution << endl;

    return 0;
}