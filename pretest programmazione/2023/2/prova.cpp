using namespace std;
#include <iostream>
#include <vector> // Necessaria per std::vector
#include <random>
#include <algorithm>

struct task
{
    int id;
    string flag;
    int punti;
};

struct submission
{
    int id_player;
    int task;
    string flag;
    int timestamp;
};

struct player
{
    int id;
    int punti;
    int last_sub;
};

bool confronta(player a, player b)
{
    if(a.punti == b.punti)
    {
        if(a.last_sub == b.last_sub)
        {
            return a.id < b.id;
        }
        return a.last_sub < b.last_sub;
    }
    return a.punti > b.punti;
}

int main()
{
    int M, N, S;
    cout << "Inserisci numero player" <<endl;
    cin >> M;
    cout << "Inserisci numero task" <<endl;
    cin >> N;
    cout << "Inserisci numero invii" <<endl;
    cin >> S;

    vector <task> task(N);
    vector <submission> sub(S);
    vector <player> player(M);

    for(int i=0;i<M;i++)
    {
        player[i].id = i+1;
        player[i].punti = 0;
        player[i].last_sub = 0;
    }

    cout << "Inserisci id task, flag task, punti task" <<endl;
    for (int i=0;i<N;i++)
    {
        cout << "Inserisci id task" <<endl;
        cout << "Inserisci flag task" <<endl;
        cout << "Inserisci punti task" <<endl;
        cin >> task[i].id >> task[i].flag >> task[i].punti;
    }

    for (int i=0;i<S;i++)
    {
        cout << "Inserisci id player" <<endl;
        cout << "Inserisci task player" <<endl;
        cout << "Inserisci flag player" <<endl;
        cout << "Inserisci timestamp player" <<endl;
        cin >> sub[i].id_player >> sub[i].task >> sub[i].flag >> sub[i].timestamp;
    }

    for(int i=0;i<S;i++)
    {
        for(int j=0;j<N;j++)
        {
            if(sub[i].flag == task[j].flag && sub[i].task == task[j].id)
            {
                player[sub[i].id_player-1].punti += task[j].punti;
                player[sub[i].id_player-1].last_sub = sub[i].timestamp;
            }
        }
    }

    //sort per punti decrescente, poi timestamp crescente poi id crescente
    sort(player.begin(), player.end(),confronta);

    for(int i=0;i<M;i++)
    {
        cout << "Player " << player[i].id << " ha totalizzato " << player[i].punti << " punti" <<endl;
    }


}