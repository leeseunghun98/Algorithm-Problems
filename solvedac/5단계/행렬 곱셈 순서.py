import sys
input = sys.stdin.readline
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
if n <= 1:
    print(0)
elif n == 2:
    print(li[0][0]*li[0][1]*li[1][1])
else:
    answer = 0
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0] = [0, li[0][0], li[0][1]]
    dp[1] = [li[0][0]*li[0][1]*li[1][1], li[0][0], li[1][1]]
    for i in range(2, n):
        a = dp[i-1][0] + dp[i-1][1]*dp[i-1][2]*li[i][1]
        b = dp[i-2][0] + li[i-1][0]*li[i-1][1]*li[i][1] + dp[i-2][1]*dp[i-2][2]*li[i][1]
        if a > b:
            c, d = dp[i-2][1], li[i][1]
        else:
            c, d = dp[i-1][1], li[i][1]
        dp[i] = [min(a, b),  c, d]
    print(dp[-1][0])
    print(dp)