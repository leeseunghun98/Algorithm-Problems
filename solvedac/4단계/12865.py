import sys
n, k = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] for _ in range(k+1)]
for i in range(1, k+1):
    for idx, j in enumerate(li):
        if i - j[0] > -1 and dp[i][0] < dp[i-j[0]][0] + j[1] and (idx not in dp[i-j[0]][1:]):
            dp[i] = dp[i-j[0]] + [idx]
            dp[i][0] = dp[i-j[0]][0] + j[1]
result = 0
for i in dp:
    if result < i[0]:
        result = i[0]
print(result)