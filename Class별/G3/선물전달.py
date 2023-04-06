n = int(input())
dp = [0 for _ in range(n+1)]
if n >= 2:
    dp[2] = 1
    if n >= 3:
        dp[3] = 2
for i in range(3, n+1):
    dp[i] = ((dp[i-1] + dp[i-2]) * (i-1)) % 1000000000
print(dp[-1])