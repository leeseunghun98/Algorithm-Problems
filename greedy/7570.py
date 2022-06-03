import sys
n = int(sys.stdin.readline().strip())
li = list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * n
for i in range(n):
    for j in range(i):
        if li[i] == li[j] + 1 and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(n - 1 - max(dp))
