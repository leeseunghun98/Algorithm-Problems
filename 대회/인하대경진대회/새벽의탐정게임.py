import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
li = list(list(sys.stdin.readline().strip()) for _ in range(n))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
state = [[4, 2, 3, 1], [1, 1, 0, 5], [0, 5, 2, 2], [3, 3, 5, 0], [5, 0, 4, 4], [2, 4, 1, 3]]
def bfs(x, y):
    queue = deque()
    queue.append([[x, y, 0, x, y]])
    cnt = 0
    while queue:
        j = queue.popleft()
        cnt += 1
        b = []
        for q in j:
            for i in range(4):
                nx = dx[i] + q[0]
                ny = dy[i] + q[1]
                if (0<=nx<n) and (0<=ny<m) and (li[nx][ny] == '.' or li[nx][ny] == 'D') and not (nx == q[3] and ny == q[4]):
                    b.append([nx, ny, state[q[2]][i], q[0], q[1]])
                elif li[nx][ny] == 'R' and state[q[2]][i] == 0:
                    return cnt
        if len(b) > 0:
            queue.append(b)
    return -1
x_pos = -1
y_pos = -1
for i in range(n):
    for j in range(m):
        if li[i][j] == 'D':
            x_pos = i
            y_pos = j
            break
    if x_pos > -1:
        break
print(bfs(x_pos, y_pos))