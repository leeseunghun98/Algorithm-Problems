import sys
input = sys.stdin.readline
testcase = int(input().strip())
dp = [0] * 46
dp[1], dp[2] = 1, 1
for i in range(3, 46):
    dp[i] = dp[i-1] + dp[i-2]
for _ in range(testcase):
    n = int(input().strip())
    a = []
    while n > 0:
        idx = 2
        while dp[idx] <= n:
            idx += 1
        n -= dp[idx-1]
        a.append(dp[idx-1])
    for i in sorted(a):
        print(i, end=" ")
    print()