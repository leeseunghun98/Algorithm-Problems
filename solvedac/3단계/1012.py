import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, graph):
    graph[x][y] = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if (0<=nx<n) and (0<=ny<m) and graph[nx][ny] == 1:
            dfs(nx, ny, graph)
for _ in range(int(input().strip())):
    m, n, k = map(int, input().strip().split())
    cabbage = [list(map(int, input().strip().split())) for _ in range(k)]
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for i in cabbage:
        graph[i[1]][i[0]] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j, graph)
                result += 1
    print(result)