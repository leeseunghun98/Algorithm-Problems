import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    dp[i] = dp[i-1] + li[i-1]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[b] - dp[a-1])