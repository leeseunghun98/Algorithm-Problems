#include <iostream>

using namespace std;
void aris(bool* arr, int length)
{
    int index = 1;
    while (++index < length)
    {
        if (!arr[index])
        {
            int offset = 1;
            while (++offset * index < length)
            {
                arr[offset*index] = 1;
            }
        }
    }

    arr[2] = 0;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int start, finish;
    cin >> start;
    cin >> finish;

    bool arr[1000001] = {false};
    aris(arr, 1000001);

    for (int i = (2 < start) ? start : 2; i <= finish; ++i)
    {
        if (!arr[i]) cout << i << '\n';
    }

    return 0;
}