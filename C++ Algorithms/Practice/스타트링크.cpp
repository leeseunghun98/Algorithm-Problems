#include "iostream"
#include "vector"
#include "queue"
using namespace std;

int s, g, d, u, f;
vector<int> dp;

int bfs()
{
    queue<int> q;
    q.push(s);
    dp[s] = 1;
    while(!q.empty())
    {
        int now = q.front();
        q.pop();

        if (now + u <= f && !dp[now + u])
        {
            q.push(now + u);
            dp[now + u] = dp[now] + 1;
        }
        if (now - d > 0 && !dp[now - d])
        {
            q.push(now - d);
            dp[now - d] = dp[now] + 1;
        }
        if (dp[g])
        {
            return dp[g];
        }
    }
    return 0;
}

int main()
{
    // S -> G, 총 F층, U업, D다운
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> f >> s >> g >> u >> d;
    dp.resize(f+1);
    
    if (int ret = bfs())
    {
        cout << ret-1 << "\n";
    }
    else
    {
        cout << "use the stairs" << "\n";
    }

    return 0;
}