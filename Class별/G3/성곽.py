import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
boundary_chk = lambda x, y : True if (0<=x<n) and (0<=y<m) else False

li = [tuple(map(int, input().split())) for _ in range(n)]

def chk_room(x, y):
    global rooms_cnt
    cnt = 0
    queue = deque([(x, y)])
    visited[x][y] = rooms_cnt + 1
    while queue:
        a, b = queue.popleft()
        cnt += 1
        if not (li[a][b] & 1) and not visited[a][b-1]:
            queue.append((a, b-1))
            visited[a][b-1] = rooms_cnt + 1
        if not (li[a][b] & 2) and not visited[a-1][b]:
            queue.append((a-1, b))
            visited[a-1][b] = rooms_cnt + 1
        if not (li[a][b] & 4) and not visited[a][b+1]:
            queue.append((a, b+1))
            visited[a][b+1] = rooms_cnt + 1
        if not (li[a][b] & 8) and not visited[a+1][b]:
            queue.append((a+1, b))
            visited[a+1][b] = rooms_cnt + 1

    return cnt

visited = [[0 for _ in range(m)] for _ in range(n)]
rooms_cnt = 0
rooms = []
for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            rooms.append(chk_room(x, y))
            rooms_cnt += 1

neighbors = [0 for _ in range(rooms_cnt+1)]
for x in range(n):
    for y in range(m):
        if boundary_chk(x+1, y) and visited[x][y] != visited[x+1][y] and neighbors[visited[x][y]] < rooms[visited[x+1][y]-1]:
            neighbors[visited[x][y]] = rooms[visited[x+1][y]-1]
        if boundary_chk(x-1, y) and visited[x][y] != visited[x-1][y] and neighbors[visited[x][y]] < rooms[visited[x-1][y]-1]:
            neighbors[visited[x][y]] = rooms[visited[x-1][y]-1]
        if boundary_chk(x, y-1) and visited[x][y] != visited[x][y-1] and neighbors[visited[x][y]] < rooms[visited[x][y-1]-1]:
            neighbors[visited[x][y]] = rooms[visited[x][y-1]-1]
        if boundary_chk(x, y+1) and visited[x][y] != visited[x][y+1] and neighbors[visited[x][y]] < rooms[visited[x][y+1]-1]:
            neighbors[visited[x][y]] = rooms[visited[x][y+1]-1]

for i in range(1, rooms_cnt+1):
    neighbors[i] += rooms[i-1]

print(rooms_cnt)
print(max(rooms))
print(max(neighbors))