import sys
n = int(sys.stdin.readline().strip())
li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(n):
    for j in range(2, n):
        if li[i][j] == 1 or (li[i-1][j] == 1 and li[i][j-1] == 1):
            continue
        elif li[i-1][j] == 1 and li[i-1][j-1] == 0 and li[i][j-1] == 0:
            dp[i][j] = [dp[i][j-1][0] + dp[i][j-1][1], 0, 0]
        elif li[i-1][j] == 0 and li[i-1][j-1] == 1 and li[i][j-1] == 0:
            dp[i][j] = [dp[i][j-1][0], 0, dp[i-1][j][2]]
        elif li[i-1][j] == 0 and li[i-1][j-1] == 0 and li[i][j-1] == 1:
            dp[i][j] = [0, 0, dp[i-1][j][1] + dp[i-1][j][2]]
        elif li[i-1][j] == 1 and li[i-1][j-1] == 1 and li[i][j-1] == 0:
            dp[i][j] = [dp[i][j-1][0], 0, 0]
        elif li[i-1][j] == 0 and li[i-1][j-1] == 1 and li[i][j-1] == 1:
            dp[i][j] = [0, 0, dp[i-1][j][2]]
        else:
            dp[i][j] = [dp[i][j-1][0] + dp[i][j-1][1], sum(dp[i-1][j-1]), dp[i-1][j][1] + dp[i-1][j][2]]
print(sum(dp[n-1][n-1]))