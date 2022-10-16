import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, graph, cnt):
    graph[x][y] = cnt
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if (0<=nx<n) and (0<=ny<m) and graph[nx][ny] == 1:
            cnt += 1
            dfs(nx, ny, graph, cnt)
re_cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            re_cnt += 1
            dfs(i, j, graph, 2)
print(re_cnt)
print(max(map(max, graph))-1 if max(map(max, graph))-1 != -1 else 0)