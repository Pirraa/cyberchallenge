#include <stdio.h>
#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <map>

using namespace std;

long long emulate(vector<string> code){
    // SCRIVI QUA IL TUO CODICE
    int lettere[6] = {0,0,0,0,0,0};
    map <string, int> label;
    int a = 0, b = 0, c = 0, d = 0, e = 0, f = 0;
    //jmp d 55 gq
    int i=0;
    for(i;i<code.size();i++)
    {
        //cout << "riga i: " << i << endl;
        //leggo riga e splitto per spazio in 3 parti
        //switch su prima parte con operazione da fare mul add o sub
        //in ogni ramo dello switch leggo seconda parte con variabile da modificare
        //leggo terza parte e faccio operazione sulla variabile

        //splitto riga
        string s = code[i];
        string parts[4];
        int n=3;
        for(int j=0;j<n;j++)
        {
            parts[j]=s.substr(0,s.find(" "));
            if(parts[0]=="lab")
                n=2;
            else if(parts[0]=="jmp")
            {
                n=4;
                //cout << "jmp" << endl;
            }
                
            s.erase(0,s.find(" ")+1);
        }
        //cout << "riga letta" << parts[0] << " " << parts[1] << " " << parts[2] << " " << parts[3] << endl;
        string operation;
        pair<string,int> coppia;
        switch(parts[0][0])
        {
            case 'm':
                operation = "mul";
                break;
            case 'a':
                operation = "add";
                break;
            case 's':
                operation = "sub";
                break;
            case 'l':
                coppia = make_pair(parts[1], i);
                //cout << "coppia: " << coppia.first << " " << coppia.second << endl;
                label.insert(coppia);
                operation = "label";
                break;
            case 'j':
                operation = "jmp";
                break;
        }
        //cout << "operazione selezionata" << operation << endl;

        if(operation == "label")
            continue;

        if(operation == "jmp")
        {
            //controllo se parts[2] corrisponde al valore della lettera in parts[1]
            int valore;
            switch(parts[1][0])
            {
                case 'a':
                    valore = a;
                    break;
                case 'b':
                    valore = b;
                    break;
                case 'c':
                    valore = c;
                    break;
                case 'd':
                    valore = d;
                    break;
                case 'e':
                    valore = e;
                    break;
                case 'f':
                    valore = f;
                    break;
            }
            //cout << "valore: " << valore << endl;
            
            if(valore == stoi(parts[2]))
            {
                //cout << parts[3] << endl;
                auto it = label.find(parts[3]);
                if (it != label.end()) {
                    i = it->second;
                    //cout << "i: " << i << endl;
                } else {
                    //cout << "Label not found: " << parts[3] << endl;
                }
            }
        }
        switch(parts[1][0])
        {
            case 'a':
                if(operation == "mul")
                {
                    a = a * stoi(parts[2]);
                }
                else if(operation == "add")
                {
                    a = a + stoi(parts[2]);
                }
                else if(operation == "sub")
                {
                    a = a - stoi(parts[2]);
                }
            break;
            case 'b':
                if(operation == "mul")
                {
                    b = b * stoi(parts[2]);
                }
                else if(operation == "add")
                {
                    b = b + stoi(parts[2]);
                }
                else if(operation == "sub")
                {
                    b = b - stoi(parts[2]);
                }
            break;
            case 'c':
                if(operation == "mul")
                {
                    c = c * stoi(parts[2]);
                }
                else if(operation == "add")
                {
                    c = c + stoi(parts[2]);
                }
                else if(operation == "sub")
                {
                    c = c - stoi(parts[2]);
                }
            break;
            case 'd':
                if(operation == "mul")
                {
                    d = d * stoi(parts[2]);
                }
                else if(operation == "add")
                {
                    d = d + stoi(parts[2]);
                }
                else if(operation == "sub")
                {
                    d = d - stoi(parts[2]);
                }
            break;
            case 'e':
                if(operation == "mul")
                {
                    e = e * stoi(parts[2]);
                }
                else if(operation == "add")
                {
                    e = e + stoi(parts[2]);
                }
                else if(operation == "sub")
                {
                    e = e - stoi(parts[2]);
                }
            break;
            case 'f':
                if(operation == "mul")
                {
                    f = f * stoi(parts[2]);
                }
                else if(operation == "add")
                {
                    f = f + stoi(parts[2]);
                }
                else if(operation == "sub")
                {
                    f = f - stoi(parts[2]);
                }
            break;
            }
        //cout << "a: " << a << " b: " << b << " c: " << c << " d: " << d << " e: " << e << " f: " << f << endl;
    }
    return a + b + c + d + e + f;
}

int main()
{

    freopen("2024-emulation_emulation-2_1737996040.txt", "r", stdin); // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
    freopen("output.txt", "w", stdout); // DECOMMENTA QUA SE VUOI SCRIVERE DA FILE

    int N;
    vector<string> code;
    string s;
    cin >> N;
    getline(cin, s);

    for(int i = 0; i < N; i++){
        getline(cin, s);
        code.push_back(s);
    }

    cout << emulate(code) << endl;

    return 0;
}