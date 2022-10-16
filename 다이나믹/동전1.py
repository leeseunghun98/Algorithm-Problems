import sys
input = sys.stdin.readline
n, target = map(int, input().split())
coins = [0] + sorted([int(input()) for _ in range(n)])
dp = [[1] + [0 for _ in range(target)] for _ in range(2)]

for i in range(1, n+1):
    for j in range(1, target+1):
        if coins[i] > j:
            dp[1][j] = dp[0][j]
            continue
        dp[1][j] = dp[0][j] + dp[1][j-coins[i]]
    dp[0] = dp[1]

print(dp[-1][-1])