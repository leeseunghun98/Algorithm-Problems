import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
li = [list(input().rstrip()) for _ in range(n)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
chk = lambda x, y: True if (0<=x<n) and (0<=y<m) else False

waters = []
for x in range(n):
    for y in range(m):
        if li[x][y] == '*':
            waters.append((x, y))
        elif li[x][y] == 'S':
            s = (x, y)
        elif li[x][y] == 'D':
            d = (x, y)

queue = deque(waters)
dist = [[2500 for _ in range(m)] for _ in range(n)]
for i in waters:
    dist[i[0]][i[1]] = 1
cnt = 2
while queue:
    next_queue = deque([])
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if chk(nx, ny) and dist[nx][ny] == 2500 and (li[nx][ny] != 'X' and li[nx][ny] != 'D'):
                dist[nx][ny] = cnt
                next_queue.append((nx, ny))
    queue = next_queue
    cnt += 1

queue = deque([s])
dist[s[0]][s[1]] = 0

turn = 2
answer = 0
while queue:
    next_queue = deque([])
    while queue:
        a, b = queue.popleft()
        if li[a][b] == 'D':
            answer = turn - 2
            break
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if chk(nx, ny) and ((dist[nx][ny] > turn and li[nx][ny] == '.') or li[nx][ny] == 'D'):
                dist[nx][ny] = 0
                next_queue.append((nx, ny))
    if answer:
        break
    queue = next_queue
    turn += 1
print(answer if answer > 0 else 'KAKTUS')