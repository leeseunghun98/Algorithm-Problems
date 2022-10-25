import sys
from collections import deque
s = "0" + sys.stdin.readline().rstrip()
n = len(s) - 1
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n, 0, -1):
    for j in range(i, n+1):
        if i == j:
            dp[i][j] = 1
        elif i + 1 == j:
            if s[i] == s[j]:
                dp[i][j] = 1
        else:
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]

ddp = [2500 for _ in range(n+2)]
ddp[1] = 0
for finish in range(1, n+1):
    for start in range(1, finish+1):
        if dp[start][finish]:
            ddp[finish+1] = min(ddp[finish+1], ddp[start]+1)
    ddp[finish+1] = min(ddp[finish+1], ddp[finish]+1)

print(ddp[-1])