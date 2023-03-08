import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
li = [tuple(map(int, input().split())) for _ in range(n)]
chk = lambda x, y: True if (0<=x<n) and (0<=y<n) else False
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
virus = []
zeros = 0
for i in range(n):
    for j in range(n):
        if li[i][j] == 0:
            zeros += 1
        elif li[i][j] == 2:
            zeros += 1
            virus.append((i, j))

answer = 2500
for com in combinations(virus, m):
    queue = deque(com)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in com:
        visited[i[0]][i[1]] = 1
    cnt = 0
    zero = len(virus)
    while queue:
        if zero == zeros:
            break
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if chk(nx, ny) and not visited[nx][ny] and li[nx][ny] != 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    if li[nx][ny] == 0:
                        zero += 1
        cnt += 1
    if zero == zeros and answer > cnt:
        answer = cnt
print(answer if answer < 2500 else -1)