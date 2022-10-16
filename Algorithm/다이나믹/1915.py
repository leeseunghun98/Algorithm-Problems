import sys
n, m = map(int, sys.stdin.readline().strip().split())
li = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
for i in range(1, m):
    li[0][i] += li[0][i-1]
for i in range(1, n):
    li[i][0] += li[i-1][0]
for i in range(1, n):
    for j in range(1, m):
        li[i][j] = li[i][j] + li[i-1][j] + li[i][j-1] -li[i-1][j-1]
for i in range(n):
    for 