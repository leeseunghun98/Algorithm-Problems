import sys
from collections import deque
n = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
size = 2
def bfs(x, y, graph):
    global size
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    queue = deque()
    queue.append([[x, y, 1, 0]])
    cnt = 0
    ate_cnt = 0
    while queue:
        li = []
        k = queue.popleft()
        for j in k:
            for i in range(4):
                nx = dx[i] + j[0]
                ny = dy[i] + j[1]
                if (0<=nx<n) and (0<=ny<n) and visited[nx][ny] == 0:
                    if graph[nx][ny] == 0 or graph[nx][ny] == size:
                        visited[nx][ny] = 1
                        li.append([nx, ny, j[2] + 1, 0])
                    elif graph[nx][ny] < size:
                        visited[nx][ny] = 1
                        li.append([nx, ny, j[2], 1])
                        break
        li.sort(key=lambda x:x[1])
        li.sort(key=lambda x:x[0])
        cx, cy, cc = 0, 0, 0
        for i in li:
            if i[3] == 1:
                cx = i[0]
                cy = i[1]
                cc = i[2]
                break
        if cc != 0:
            graph[cx][cy] = 0
            ate_cnt += 1
            if ate_cnt >= size:
                size += 1
                ate_cnt = 0
            cnt += cc
            visited = [[0 for _ in range(n)] for _ in range(n)]
            queue = deque()
            queue.append([[cx, cy, 1]])
        elif li:
            queue.append(li)
    return cnt
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j
            break
graph[x][y] = 0
print(bfs(x, y, graph))