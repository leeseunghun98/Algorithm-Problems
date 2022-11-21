#include "iostream"
#include "vector"
#include "string"

using namespace std;

int n;
vector<char> vec;
vector<bool> used(10);
long long max_num = 0;
long long min_num = 9876543210;

void dfs(int index, long long number)
{
    if (index == n)
    {
        if (number > max_num) max_num = number;
        if (number < min_num) min_num = number;
        return;
    }
    int now = number % 10;
    used[now] = 1;
    if (vec[index] == '>')
    {
        for (int i = now-1; i >= 0; --i)
        {
            if (!used[i])
            {
                dfs(index + 1, 10*number + i);
            }
        }
    }
    else
    {
        for (int i = now+1; i < 10; ++i)
        {
            if (!used[i])
            {
                dfs(index + 1, 10*number + i);
            }
        }
    }
    used[now] = 0;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> n;
    vec.resize(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> vec[i];
    }

    for (int i = 0; i < 10; ++i)
    {
        dfs(0, i);
    }
    char prev = cout.fill('0');
    cout.width(n+1);
    cout << to_string(max_num) << '\n';
    cout.fill(prev);
    prev = cout.fill('0');
    cout.width(n+1);
    cout << to_string(min_num) << '\n';
    cout.fill(prev);

    return 0;
}