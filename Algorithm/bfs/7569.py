import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().strip().split())
graph = []
for i in range(h):
    graph.append([list(map(int, input().strip().split())) for _ in range(n)])
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]
def bfs(starts, graph):
    queue = deque()
    queue.append(starts)
    cnt = 0
    while queue:
        j = queue.popleft()
        lst = []
        for a in j:
            for i in range(6):
                nx = dx[i] + a[0]
                ny = dy[i] + a[1]
                nz = dz[i] + a[2]
                if (0<=nx<h) and (0<=ny<n) and (0<=nz<m) and graph[nx][ny][nz] == 0:
                    lst.append([nx, ny, nz])
                    graph[nx][ny][nz] = 1
        if len(lst) > 0:
            queue.append(lst)
            cnt += 1
        else:
            return cnt
starts = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                starts.append([i, j, k])
result = bfs(starts, graph)
zero = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                zero = 1
print(result if zero == 0 else -1)