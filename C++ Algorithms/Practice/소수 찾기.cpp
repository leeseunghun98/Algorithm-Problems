#include <cstdio>
#include <cmath>
using namespace std;

bool IsPrime(int n)
{
    if (n == 1) return false;

    for (int i = 2; i < int(sqrt(n)+1); ++i)
    {
        if (n % i == 0) return false;
    }

    return true;
}

int main()
{
    int n;
    int answer = 0;
    scanf("%d", &n);
    int* arr = new int[n];
    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < n; ++i)
    {
        if (IsPrime(arr[i])) answer += 1;
    }

    printf("%d", answer);
    
    return 0;
}