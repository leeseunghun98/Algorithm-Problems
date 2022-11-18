import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
boundary_chk = lambda x, y : True if (0<=x<n) and (0<=y<n) else False
li = [list(map(int, input().split())) for _ in range(n)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

starts = []
country_number = 2

def find_country(x, y):
    queue = deque([(x, y)])
    li[x][y] = country_number
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if boundary_chk(nx, ny):
                if li[nx][ny] == 1:
                    li[nx][ny] = country_number
                    queue.append((nx, ny))
                elif li[nx][ny] == 0:
                    starts.append((country_number, nx, ny, 1))

for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            find_country(i, j)
            country_number += 1

queue = deque(starts)
ans_cnt = 1
answer = int(1e6)
while queue:
    c_num, x, y, cnt = queue.popleft()
    if cnt > ans_cnt:
        if answer != int(1e6):
            break
        ans_cnt = cnt
    if li[x][y] == c_num:
        continue
    if li[x][y] != 0:
        if li[x][y] > c_num:
            answer = min(answer, 2*cnt-2)
        else:
            answer = min(answer, 2*cnt-1)
    li[x][y] = c_num
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if boundary_chk(nx, ny) and li[nx][ny] != c_num:
            queue.append((c_num, nx, ny, cnt+1))
print(answer)