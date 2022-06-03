import sys
n = int(sys.stdin.readline().strip())
li = list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    for j in range(i):
        if li[i] < li[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
    if dp[i] == 0:
        dp[i] = 1
print(max(dp))