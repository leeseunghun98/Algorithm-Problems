import sys
n, k = map(int, sys.stdin.readline().strip().split())
li = [int(sys.stdin.readline().strip()) for _ in range(n)]
dp = [[0 for _ in range(k+1)] for _ in range(2)]
for i in range(n):
    for j in range(0, k+1):
        if i == 0:
            if j % li[i] == 0:
                dp[1][j] = 1
            continue
        if j >= li[i]:
            dp[1][j] = dp[0][j] + dp[1][j-li[i]]
        else:
            dp[1][j] = dp[0][j]
    for i in range(k+1):
        dp[0][i] = dp[1][i]
print(max(max(dp[1]), max(dp[0])))