#include <stdio.h>
#include <iostream>
#include <vector>
#include <array>

using namespace std;

long long find_sum_of_times(int N, int M, vector<int> t, vector<int> f, vector<int> emails){
    // WRITE YOUR CODE HERE
    long long sum = 0;
    long long timeMail=0;
    //per ogni email
    for(int i=0; i<M; i++)
    {
        timeMail = emails[i];
        //per ogni server
        for(int j=0; j<N; j++)
        {
            //aumento il tempo della mail sostituendolo con il multiplo più vicino a t[j]
            //poi sommo a tale tempo il tempo di invio cioè f[j]
            /*for(int k=timeMail; k<timeMail+t[j]; k++)
            {
                if(k%t[j] == 0)
                {
                    timeMail = k;
                    break;
                }
            }*/
           //vado al mutiplo più vicino a timemail sommando t[j], tolgo 1 così se timemail è già un multiplo sono 1 sotto al multiplo successivo
           //diviso con divisione intera per t[j] così ottengo il numeri di multipli di t[j] fino al numero ottenuto prima
           //moltiplicando il numero di multipli per t[j] ottengo il multiplo più vicino a timemail
           //esempio timemail=16, t[j]=7 -> 16+7-1=22, 22/7=3, 3*7=21
            timeMail = ((timeMail + t[j] - 1) / t[j]) * t[j];
            timeMail+=f[j];
            //cout << "tempo mail numero " << i << " dopo " << j<< " server " <<timeMail << " "<<endl;
        }            
        //cout << "tempo mail numero " << i << " " <<timeMail << " "<<endl;
        sum += timeMail;
    }
    return sum;
}

int main(){
    freopen("2025-emails_emails-3_1738079876.txt", "r", stdin); // DECOMMENT IF YOU WANT TO READ FROM FILE
    freopen("output1.txt", "w", stdout); // DECOMMENT IF YOU WANT TO WRITE TO FILE

    int N, M;
    cin >> N >> M;
    vector<int> t(N), f(N), emails(M);

    for(auto& x : t) cin >> x;
    for(auto& x : f) cin >> x;
    for(auto& x : emails) cin >> x;

    cout << find_sum_of_times(N, M, t, f, emails);

    return 0;
}