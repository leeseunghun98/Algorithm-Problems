import sys
N, K = map(int, sys.stdin.readline().strip().split())
dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
dp[1][0] = 1
for i in range(N+1):
    dp[1][i] = 1
dp[1][1] = 1
for i in range(2, K+1):
    for j in range(N+1):
        dp[i][j] = sum(dp[i-1][:j+1])%1000000000
print(dp[-1][-1])
