import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
boundary_chk = lambda x, y : True if (0<=x<n) and (0<=y<n) else False
li = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def solve(x, y):
    ret = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if boundary_chk(nx, ny) and li[nx][ny] > li[x][y]:
            if not dp[nx][ny]:
                solve(nx, ny)
            ret = max(ret, dp[nx][ny])
    dp[x][y] = ret+1

for i in range(n):
    for j in range(n):
        if not dp[i][j]:
            solve(i, j)

answer = 0
for i in dp:
    answer = max(answer, max(i))
print(answer)