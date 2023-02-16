import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
li = [[0 for _ in range(m)] for _ in range(n)]
chk = lambda x, y: True if (0<=x<n) and (0<=y<m) else False
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
for _ in range(k):
    a, b = map(int, input().split())
    li[a-1][b-1] = 1

def bfs(x, y):
    ret = 0
    li[x][y] = 0
    queue = deque([(x, y)])
    while queue:
        a, b = queue.popleft()
        ret += 1
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if chk(nx, ny) and li[nx][ny]:
                queue.append((nx, ny))
                li[nx][ny] = 0
    return ret

answer = 0
for x in range(n):
    for y in range(m):
        if li[x][y]:
            answer = max(answer, bfs(x, y))
print(answer)
