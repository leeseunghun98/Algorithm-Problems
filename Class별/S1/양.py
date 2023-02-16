import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
li = [list(input().rstrip()) for _ in range(n)]
chk = lambda x,y : True if (0<=x<n) and (0<=y<m) else False
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def solve(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    sheep = 0
    wolf = 0
    
    while queue:
        a, b = queue.popleft()
        if li[a][b] == 'o':
            sheep += 1
        elif li[a][b] == 'v':
            wolf += 1
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if chk(nx, ny) and not visited[nx][ny] and li[nx][ny] != '#':
                queue.append((nx, ny))
                visited[nx][ny] = 1
    return (sheep, 0) if sheep > wolf else (wolf, 1)


visited = [[0 for _ in range(m)] for _ in range(n)]
answer = [0, 0]
for x in range(n):
    for y in range(m):
        if not visited[x][y] and li[x][y] != '#':
            a, b = solve(x, y)
            answer[b] += a
print(*answer)