n = input().rstrip()
n = '0' + n
m = len(n)
dp = [0 for _ in range(m)]
if m == 2:
    if n[1] == '0':
        pass
    else:
        dp[-1] = 1
else:
    if n[1] != '0':
        dp[0] = 1
        dp[1] = 1
        for i in range(2, m):
            if n[i] != '0':
                dp[i] += dp[i-1]
            if (10 <= int(n[i-1:i+1]) <= 26):
                dp[i] += dp[i-2]

print(dp[-1] % 1000000)