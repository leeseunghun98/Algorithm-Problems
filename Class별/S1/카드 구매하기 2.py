import sys
input = sys.stdin.readline
n = int(input())
n += 1
li = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(1, n):
    dp[1][i] = li[1] * i
    
for i in range(2, n):
    for j in range(i):
        dp[i][j] = dp[i-1][j]
    dp[i][i] = min(li[i], dp[i-1][i], dp[i][0] + li[i])
    for j in range(i+1, n):
        dp[i][j] = min(dp[i-1][j], dp[i][j-i] + li[i])

print(dp[-1][-1])