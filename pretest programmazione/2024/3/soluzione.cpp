#include <stdio.h>
#include <iostream>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;

vector<int> getright(vector<int> S, int D)
{
    vector<int> res(S.size());
    int j = S.size() - 1;

    for (int i = S.size() - 1; i >= 0; i--)
    {
        while (j >= 0 && S[j] - S[i] > D)
            j--;
        res[i] = j;
    }
    return res;
}

vector<int> getleft(vector<int> S, int D)
{
    vector<int> res(S.size());
    int j = 0;

    for (int i = 0; i < S.size(); i++)
    {
        while (j < S.size() && S[i] - S[j] > D)
            j++;
        res[i] = j;
    }
    return res;
}

int find_subsets(int N, int D, vector<int> S)
{
    sort(S.begin(), S.end());
    vector<int> rm = getright(S, D);
    vector<int> lm = getleft(S, D);
    int ans = 0;
    vector<int> ls(N), rs(N);

    for (int i = 0; i < N; i++)
    {
        ls[i] = i - lm[i] + 1;
        if (i > 0)
            ls[i] = max(ls[i], ls[i - 1]);
    }

    for (int i = N - 1; i >= 0; i--)
    {
        rs[i] = rm[i] - i + 1;

        if (i < N - 1)
            rs[i] = max(rs[i], rs[i + 1]);
    }

    for (int i = 0; i < N - 1; i++)
        ans = max(ans, ls[i] + rs[i + 1]);

    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin); // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
    freopen("output.txt", "w", stdout); // DECOMMENTA QUA SE VUOI SCRIVERE DA FILE
    int T;
    cin >> T;

    while (T--)
    {
        int N, D;

        vector<int> S;

        cin >> N >> D;
        for (int i = 0; i < N; i++)
        {
            int x;
            cin >> x;
            S.push_back(x);
        }

        cout << find_subsets(N, D, S) << endl;
    }

    return 0;
}