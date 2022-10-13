n = int(input())
dp = [0 for _ in range(n+1)]
dp[1] = 1
for i in range(2, n+1):
    idx = 1
    ret = 50000
    while idx ** 2 <= i:
        ret = min(ret, dp[i-idx**2]+1)
        idx += 1
    dp[i] = ret
print(dp[-1])