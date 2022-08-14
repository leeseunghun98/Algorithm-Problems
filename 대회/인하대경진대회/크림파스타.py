import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
dp = [[li[0],li[0], 0] for _ in range(n)]
for i in range(1, n):
    turn = 0
    if li[i] < dp[i-1][0]:
        dp[i][0] = li[i]
        turn = 1
    else:
        dp[i][0] = dp[i-1][0]
    if li[i] > dp[i-1][1]:
        dp[i][1] = li[i]
    elif turn == 1:
        dp[i][1] = dp[i][0]
    else:
        dp[i][1] = dp[i-1][0]
    if dp[i][1] - dp[i][0] > dp[i-1][2]:
        dp[i][2] = dp[i][1] - dp[i][0]
    else:
        dp[i][2] = dp[i-1][2]
for i in dp:
    print(i[2], end=" ")