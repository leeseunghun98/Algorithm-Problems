import sys
input = sys.stdin.readline
n = int(input())
li = tuple(map(int, input().split()))
m = int(input())
marbles = tuple(map(int, input().split()))
dp = [[0 for _ in range(15001)] for _ in range(n)]

dp[0][0] = 1
dp[0][li[0]] = 1
for i in range(1, n):
    for j in range(15001):
        if dp[i-1][j]:
            dp[i][j+li[i]] = 1
            dp[i][abs(j-li[i])] = 1
            dp[i][j] = 1

for i in marbles:
    if i > 15000 or not dp[-1][i]:
        print('N', end=" ")
    else:
        print('Y', end=" ")