import sys
input = sys.stdin.readline
n = int(input().strip())
li = [list(map(int, input().strip().split())) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(2)]
dp[0] = li[0]
for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[1][0] = li[i][0] + max(dp[0][0], dp[0][1])
        elif j == 1:
            dp[1][1] = li[i][1] + max(dp[0])
        else:
            dp[1][2] = li[i][2] + max(dp[0][1], dp[0][2])
    dp[0] = [dp[1][0], dp[1][1], dp[1][2]]
print(max(dp[0]), end=" ")
for i in range(1, n):
    for j in range(3):
        if j == 0:
            li[i][0] += min(li[i-1][0], li[i-1][1])
        elif j == 1:
            li[i][1] += min(li[i-1])
        else:
            li[i][2] += min(li[i-1][1], li[i-1][2])
print(min(li[-1]))