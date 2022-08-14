import sys

def clean(lst, x, y, dir, n, m):
    global answer
    lst[x][y] = 2
    cleand = 0
    for i in range(dir+1, dir+5):
        i %= 4
        nx = dx[i] + x
        ny = dy[i] + y
        if (0 <= nx < n) and (0 <= ny < m) and lst[nx][ny] == 0:
            answer += 1
            cleand = 1
            clean(lst, nx, ny, i, n, m)
            break
    if cleand == 0:
        nx = x - dx[i]
        ny = y - dy[i]
        if (0 <= nx < n) and (0 <= ny < m) and (lst[nx][ny] == 0 or lst[nx][ny] == 2):
            if lst[nx][ny] == 0:
                answer += 1
            clean(lst, nx, ny, dir, n, m)

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 1
if d % 2:
    d += 2
    d %= 4
clean(li, r, c, d, n, m)
print(answer)