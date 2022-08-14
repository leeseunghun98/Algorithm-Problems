from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
li = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

for y in range(m):
    for x in range(n):
        if li[x][y] == 'R':
            R_pos = [x, y]
        elif li[x][y] == 'B':
            B_pos = [x, y]
        elif li[x][y] == 'O':
            O_pos = [x, y]

queue = deque()
queue.append(R_pos + B_pos + [0])
fin = 0
visited = [[[[0 for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]
visited[R_pos[0]][R_pos[1]][B_pos[0]][B_pos[1]] = 1
while queue:
    j = queue.popleft()
    if j[4] > 9:
        continue
    for i in range(4):
        a_dest = 0
        b_dest = 0
        a = 0
        while (0<=(a+1)*dx[i]+j[0]<n) and (0<=(a+1)*dy[i]+j[1]<m) and li[(a+1)*dx[i]+j[0]][(a+1)*dy[i]+j[1]] != '#':
            a += 1
            if li[a*dx[i]+j[0]][a*dy[i]+j[1]] == 'O':
                a_dest = 1
                break
        b = 0
        while (0<=(b+1)*dx[i]+j[2]<n) and (0<=(b+1)*dy[i]+j[3]<m) and li[(b+1)*dx[i]+j[2]][(b+1)*dy[i]+j[3]] != '#':
            b += 1
            if li[b*dx[i]+j[2]][b*dy[i]+j[3]] == 'O':
                b_dest = 1
                break
        if a*dx[i]+j[0] == b*dx[i]+j[2] and a*dy[i]+j[1] == b*dy[i]+j[3]:
            if a > b:
                a -= 1
            else:
                b -= 1
        if a_dest == 1 and b_dest == 0:
            print(j[4]+1)
            fin = 1
            break
        elif b_dest == 1:
            continue
        elif visited[a*dx[i]+j[0]][a*dy[i]+j[1]][b*dx[i]+j[2]][b*dy[i]+j[3]] == 0:
            visited[a*dx[i]+j[0]][a*dy[i]+j[1]][b*dx[i]+j[2]][b*dy[i]+j[3]] = 1
            queue.append([a*dx[i]+j[0], a*dy[i]+j[1], b*dx[i]+j[2], b*dy[i]+j[3], j[4] + 1])
    if fin == 1:
        break
if fin == 0:
    print(-1)
