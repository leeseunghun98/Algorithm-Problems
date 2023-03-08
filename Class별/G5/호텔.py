import sys
input = sys.stdin.readline
c, n = map(int, input().split())
li = [tuple(map(int, input().split())) for _ in range(n)]
MAX = float("inf")
dp = [MAX for _ in range(c+101)]
dp[0] = 0
for i in range(n):
    for j in range(1, c+101):
        if li[i][1] <= j:
            dp[j] = min(dp[j], dp[j - li[i][1]] + li[i][0])
print(min(dp[c:]))