import sys
input = sys.stdin.readline
n = int(input().strip())
li = [0] + list(map(int, input().strip().split()))
dp = [0] * (n+1)
for i in range(n+1):
    dp[i] = li[i]
for i in range(1, n+1):
    for j in range(1, i):
        if li[j] < li[i]:
            dp[i] = max(dp[i], dp[j] + li[i])
print(max(dp))