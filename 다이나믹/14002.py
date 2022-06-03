import sys
n = int(sys.stdin.readline().strip())
li = list(map(int, sys.stdin.readline().strip().split()))
dp = [[0, 0] for _ in range(n)]
for i in range(n):
    for j in range(i):
        if li[i] > li[j] and dp[i][0] <= dp[j][0]:
            dp[i][0] = dp[j][0] + 1
            dp[i][1] = j
    if dp[i][0] == 0:
        dp[i][0] = 1
        dp[i][1] = -1
idx = 0
for i in range(n):
    if dp[idx][0] < dp[i][0]:
        idx = i
print(dp[idx][0])
a = []
while dp[idx][1] != -1:
    a.append(li[idx])
    idx = dp[idx][1]
a.append(li[idx])
for i in sorted(a):
    print(i, end=" ")