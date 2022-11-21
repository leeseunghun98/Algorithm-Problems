#include "iostream"
#include "vector"
#include "string"

using namespace std;

int n, m;
vector<string> board;
vector<vector<bool>> visited;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

void clear()
{
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            visited[i][j] = 0;
        }
    }
}

int bfs(int x, int y)
{
    vector<pair<int, int>>* vec;
    vector<pair<int, int>> v;
    v.push_back(make_pair(x, y));
    visited[x][y] = 1;
    vec = &v;
    int cnt = -1;
    while (!vec->empty())
    {
        ++cnt;
        vector<pair<int, int>>* v_in = new vector<pair<int, int>>;

        for (int i = 0; i < vec->size(); ++i)
        {
            int a = (*vec)[i].first;
            int b = (*vec)[i].second;

            for (int dir = 0; dir < 4; ++dir)
            {
                int nx = dx[dir] + a;
                int ny = dy[dir] + b;

                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && board[nx][ny] == 'L')
                {
                    v_in->push_back(make_pair(nx, ny));
                    visited[nx][ny] = 1;
                }
            }
        }

        vec = v_in;
    }

    clear();
    return cnt;
} 

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    cin >> n >> m;
    int ret;
    int answer = 0;

    for (int i = 0; i < n; ++i)
    {
        string s;
        cin >> s;
        board.push_back(s);
    }

    for (int i = 0; i < n; ++i)
    {
        visited.push_back(vector<bool> (m));
    }

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            if (board[i][j] == 'L')
            {
                ret = bfs(i, j);
                if (answer < ret) answer = ret;
            }
        }
    }
    cout << answer << '\n';

    return 0;
}