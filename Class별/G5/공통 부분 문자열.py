import sys
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()
dp = [[0 for _ in range(len(b))] for _ in range(len(a))]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 1
mx = 0
for i in dp:
    mx = max(mx, max(i))
print(mx)