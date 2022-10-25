import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
li = [tuple(input().rstrip()) for _ in range(n)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
boundary_chk = lambda x, y : True if (0<=x<n) and (0<=y<m) else False

visited = [[0 for _ in range(m)] for _ in range(n)]
def bfs(x, y, mode):
    queue = deque([(x, y)])
    visited[x][y] = 1
    cnt = 0
    while queue:
        i, j = queue.popleft()
        cnt += 1
        for q in range(4):
            nx = dx[q] + i
            ny = dy[q] + j
            if boundary_chk(nx, ny) and not visited[nx][ny]:
                if mode:
                    if li[nx][ny] == 'B':
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                elif li[nx][ny] == 'W':
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    return cnt

answer = [0, 0]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if li[i][j] == 'W':
                answer[0] += bfs(i, j, 0) ** 2
            else:
                answer[1] += bfs(i, j, 1) ** 2
print(*answer)