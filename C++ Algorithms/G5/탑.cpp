#include "iostream"
#include "vector"
#include "stack"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int n;
    vector<int> vec;
    stack<pair<int, int>> stack;

    cin >> n;
    vec.resize(n);
    
    for (int i = 0; i < n; ++i)
    {
        cin >> vec[i];
    }

    for (int i = 0; i < n; ++i)
    {
        while (!stack.empty() && stack.top().first < vec[i])
        {
            stack.pop();
        }

        if (stack.size() > 0)
        {
            cout << stack.top().second << ' ';
        }
        else
        {
            cout << 0 << ' ';
        }

        stack.push(make_pair(vec[i], i+1));
    }

    return 0;
}