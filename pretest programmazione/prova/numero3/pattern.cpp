#include <stdio.h>
#include <iostream>
#include <vector>
#include <array>

using namespace std;

int count_patterns(int N, int M, string alph, string s){
    int count=0;
    for(int i=1; i<M;i++)
    {
        if(M%i!=0)
            continue;
        //prendo tutte le possibili sottostringhe di alph di lunghezza i
        //controllo se ripetendole M/i volte ottengo s
        string sub=s.substr(0,i);
        string repeat="";

        for(int j=0;j<M/i;j++)
            repeat+=sub;

        if(repeat==s)
            count++;
    }
    return count;
}

int main()
{

    freopen("input1.txt", "r", stdin); // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
    freopen("output.txt", "w", stdout); // DECOMMENTA QUA SE VUOI SCRIVERE DA FILE
    int T;
    cin >> T;

    while(T--){
        int N, M;
        string alph, s;

        cin >> N >> M;
        cin >> alph >> s;
        cout << count_patterns(N, M, alph, s) << endl;
    }

    return 0;
}