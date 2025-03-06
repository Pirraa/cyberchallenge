#include <stdio.h>
#include <iostream>
#include <vector>
#include <array>
#include <string>

using namespace std;

string execute_code(int N, vector<string> code){
    // WRITE YOUR CODE HERE
    string characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    string result="";

   for(int i=0;i<N;i++)
   {
        string s = code[i];
        string parts[3];
        int n=3;
        for(int j=0;j<n;j++)
        {
            parts[j]=s.substr(0,s.find(" "));  
            if(parts[0]=="add" || parts[0]=="rot")
                n=2;
            else if(parts[0]=="del")
                n=1;
            s.erase(0,s.find(" ")+1);
            //cout << parts[j] << endl;
        }
        //cout <<parts[0] << endl;
        if(parts[0]=="add")
            result.push_back(parts[1][0]);
        else if(parts[0]=="del" && !result.empty())
            result.pop_back();
        else if(parts[0]=="rot")
        {
            //rot 21-> manda avanti di 21 nell'array result sulla base della posizone nell'array characters
            int shift = stoi(parts[1]);
            for(int i=0;i<result.size();i++)
            {
                //possibile ottimizzazione con mappa di rotazione
                int pos = characters.find(result[i]);
                pos = (pos+shift)%characters.size();
                result[i]=characters[pos];
            }
        }else if(parts[0]=="swap")
        {
            //swap a F scambia la a con la F e viceversa
            char a = parts[1][0];
            char b = parts[2][0];

            for(int i=0;i<result.size();i++)
            {
                if(result[i]==a)
                    result[i]=b;
                else if(result[i]==b)
                    result[i]=a;
            }
        }
        //cout << result << endl;
   }
    return result;
}

int main(){
    freopen("2025-aliens_aliens-3_1738079586.txt", "r", stdin); // DECOMMENT IF YOU WANT TO READ FROM FILE
    freopen("output1.txt", "w", stdout); // DECOMMENT IF YOU WANT TO WRITE TO FILE

    int N;
    vector<string> code;
    cin >> N;

    string s;
    getline(cin, s);

    for(int i = 0; i < N; i++){
        getline(cin, s);
        code.push_back(s);
    }

    cout << execute_code(N, code);

    return 0;
}