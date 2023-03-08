import sys
input = sys.stdin.readline
n = 19
pan = [list(map(int, input().split())) for _ in range(n)]
chk = lambda x, y: True if (0<=x<n) and (0<=y<n) else False
dx = ((-1, 1), (0, 0), (1, -1), (1, -1))
dy = ((1, -1), (1, -1), (1, -1), (0, 0))

def five(x, y, target):
    for i in range(4):
        cnt = 0
        for j in range(2):
            nx = x + dx[i][j]
            ny = y + dy[i][j]
            while chk(nx, ny) and pan[nx][ny] == target:
                nx += dx[i][j]
                ny += dy[i][j]
                cnt += 1
        if cnt == 4:
            return True
    return False

answer = 0
for i in (1, 2):
    for y in range(n):
        for x in range(n):
            if pan[x][y] == i:
                if five(x, y, i):
                    answer = i
                    break
        if answer:
            break
    if answer:
        break
print(answer)
if answer:
    print(x+1, y+1)