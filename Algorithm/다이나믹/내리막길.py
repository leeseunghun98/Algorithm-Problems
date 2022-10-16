import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def dfs(x, y):
    if x == n-1 and y == m-1:
        dp[x][y] = 1
        return 1
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<n) and (0<=ny<m) and graph[nx][ny] < graph[x][y]:
            if dp[nx][ny] > 0:
                cnt += dp[nx][ny]
            elif dp[nx][ny] == 0:
                cnt += dfs(nx, ny)
    if cnt == 0:
        dp[x][y] = -1
    else:
        dp[x][y] = cnt
    return cnt

print(dfs(0, 0))