import sys
sys.setrecursionlimit(10**6)
r, c = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, visited, graph):
    if graph[x][y] == 1:
        visited[x][y] = -1
    else:
        visited[x][y] = 1
    if graph[x][y] == 0:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if (0<=nx<r) and (0<=ny<c) and visited[nx][ny] == 0:
                dfs(nx, ny, visited, graph)
cnt = 1
re_cnt = 0
while cnt != 0:
    cnt = 0
    dfs(0, 0, visited, graph)
    for i in range(r):
        for idx, j in enumerate(visited[i]):
            if j == -1:
                graph[i][idx] = 0
                cnt += 1
    visited = [[0 for _ in range(c)] for _ in range(r)]
    if cnt != 0:
        re_cnt += 1
        result = cnt
print(re_cnt)
print(result)