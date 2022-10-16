import sys
from collections import deque
input=sys.stdin.readline
n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

pictures = []
def bfs(x, y):
    cnt = 0
    queue = deque([(x, y)])
    li[x][y] = 0
    while queue:
        a, b = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if (0<=nx<n) and (0<=ny<m) and li[nx][ny] == 1:
                li[nx][ny] = 0
                queue.append((nx, ny))
    pictures.append(cnt)

for i in range(n):
    for j in range(m):
        if li[i][j]:
            bfs(i, j)
if not pictures:
    print(0)
    print(0)
else:
    print(len(pictures))
    print(max(pictures))
