#include <stdio.h>
#include <iostream>
#include <vector>
#include <array>

using namespace std;

vector<string> sanitize(vector<string> words, vector<string> banned){
    vector<string> answers;
    for(int i=0; i<words.size(); i++){
        string word = words[i];
        bool isBanned = false;
        for(int j=0; j<banned.size(); j++){
            string ban = banned[j];
            if(word.find(ban) != string::npos){
                isBanned = true;
                break;
            }
        }
        if(!isBanned){
            answers.push_back("SAFE");
        }else
        {
            answers.push_back("BANNED");
        }
    }
    // SCRIVI QUA IL TUO CODICE
    return answers;
}

int main()
{

    freopen("2024-sanitization_sanitization-2_1737988640.txt", "r", stdin); // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
    freopen("output.txt", "w", stdout); // DECOMMENTA QUA SE VUOI SCRIVERE DA FILE

    int N, M;
    vector<string> words, banned, answers;
    cin >> N >> M;

    for(int i = 0; i < M; i++){
        string s;
        cin >> s;
        banned.push_back(s);
    }

    for(int i = 0; i < N; i++){
        string s;
        cin >> s;
        words.push_back(s);
    }

    answers = sanitize(words, banned);

    for(auto s : answers){
        cout << s << endl;
    }

    return 0;
}