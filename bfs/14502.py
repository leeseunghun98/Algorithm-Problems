import sys
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split())
li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
graph = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(start, graph):
    queue = deque()
    queue.append(start)
    while queue:
        j = queue.popleft()
        a = []
        for k in j:
            for i in range(4):
                nx = dx[i] + k[0]
                ny = dy[i] + k[1]
                if (0<=nx<n) and (0<=ny<m) and graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    a.append([nx, ny])
        if a != []:
            queue.append(a)
q = []
result = 0 
for i in range(n):
    for j in range(m):
        if li[i][j] == 2:
            q.append([i, j])
for i in range(n*m):
    for j in range(i+1, n*m):
        for k in range(j+1, n*m):
            if li[i//m][i%m] == 0 and li[j//m][j%m] == 0 and li[k//m][k%m] == 0:
                for a in range(n):
                    for b in range(m):
                        graph[a][b]=li[a][b]
                graph[i//m][i%m] = 1
                graph[j//m][j%m] = 1
                graph[k//m][k%m] = 1
                bfs(q, graph)
                cnt = 0
                for a in range(n):
                    for b in range(m):
                        if graph[a][b] == 0:
                            cnt += 1
                if result < cnt:
                    result = cnt
print(result)