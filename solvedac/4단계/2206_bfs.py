import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
li = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visited[0][0] = [1, 1]
    queue = deque()
    queue.append([x, y, 1, 1])
    while queue:
        j = queue.popleft()
        for i in range(4):
            nx = dx[i] + j[0]
            ny = dy[i] + j[1]
            if (0<=nx<n) and (0<=ny<m):
                if li[nx][ny] == 0:
                    if nx == n-1 and ny == m-1:
                        return j[2] + 1
                    if j[3] == 1:
                        if visited[nx][ny][0] == 0:
                            visited[nx][ny][0] = [1, 1]
                            queue.append([nx, ny, j[2] + 1, 1])
                    else:
                        if visited[nx][ny][1] == 0:
                            visited[nx][ny][1] = 1
                            queue.append([nx, ny, j[2] + 1, 0])
                elif visited[nx][ny][1] == 0 and j[3] == 1:
                    visited[nx][ny][1] = 1
                    queue.append([nx, ny, j[2] + 1, 0])
    if n == 1 and m == 1:
        return 1
    return -1
print(bfs(0, 0))