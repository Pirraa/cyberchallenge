#include <stdio.h>
#include <iostream>
#include <vector>
#include <array>

using namespace std;

string find_key(int L, string s){
    vector<string> alphabet(26);
    vector<bool> found(26, false);
    for (char c = 'a'; c <= 'z'; ++c) {
        alphabet[c - 'a'] = string(1, c);
        //cout << alphabet[c - 'a'] << endl;
    }
        for(int i=0;i<26;i++){
            if(s.find(alphabet[i]) == string::npos){
                found[i] = true;
            }
        }

        /*for(int i=0;i<26;i++){
            cout << found[i] << alphabet[i] << endl;
        }*/
   
    for(int i=0;i<26;i++){
        if(found[i] == true){
            return alphabet[i];
        }
    }
}

int main(){
    freopen("2025-keyboard_keyboard-2_1738070000.txt", "r", stdin); // DECOMMENT IF YOU WANT TO READ FROM FILE
    freopen("output.txt", "w", stdout); // DECOMMENT IF YOU WANT TO WRITE TO FILE

    int N;
    cin >> N;

    while(N--){
        int L;
        string s;

        cin >> L;
        cin >> s;
        cout << find_key(L, s) << endl;
    }

    return 0;
}