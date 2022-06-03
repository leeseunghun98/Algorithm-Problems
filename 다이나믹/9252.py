import sys
a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())
dp = [[0 for _ in range(len(b))] for _ in range(len(a) + 1)]
mx_dp = [0 for _ in range(len(a))]
for i in range(1, len(a) + 1):
    for j in range(len(b)):
        if b[j] == a[i-1]:
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = max(mx_dp[:j]) + 1
            if mx_dp[j] < dp[i][j]:
                mx_dp[j] = dp[i][j]
mx = 0
for i in range(len(a)):
    for j in range(len(b)):
        if dp[i][j] > mx:
            mx = dp[i][j]
print(mx)
