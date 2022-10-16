n = int(input())
dp = [1, 3, 7]
for i in range(n-2):
    dp[0] = dp[1]
    dp[1] = dp[2]
    dp[2] = (dp[0] + 2*dp[1]) % 9901
if n < 3:
    print(dp[n])
else:
    print(dp[2])