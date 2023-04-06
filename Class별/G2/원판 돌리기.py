import sys
from collections import deque
input = sys.stdin.readline
n, m, t = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(t)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
cnt = n * m
ssum = sum(sum(i) for i in li)

def bfs(x, y):
    global ssum
    global cnt

    queue = deque([(x, y)])
    count = 0
    value = li[x][y]
    li[x][y] = -1
    while queue:
        a, b = queue.popleft()
        count += 1
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx == -1 or nx == n:
                continue
            if ny == -1:
                ny = m - 1
            elif ny == m:
                ny = 0
            if li[nx][ny] == value:
                li[nx][ny] = -1
                queue.append((nx, ny))
    cnt -= count
    ssum -= count * value

def check(check_idx):
    changed = False
    for check_idx in range(n):
        for i in range(m):
            if li[check_idx][i] == -1:
                continue
            for dir in range(4):
                nx = check_idx + dx[dir]
                ny = i + dy[dir]
                if nx == -1 or nx == n:
                    continue
                if ny == -1:
                    ny = m - 1
                elif ny == m:
                    ny = 0
                if li[nx][ny] == li[check_idx][i]:
                    bfs(check_idx, i)
                    changed = True
                    break
    return changed

def rotateList(idx, roll):
    li[idx] = li[idx][-roll:] + li[idx][:-roll]

for x, d, k in commands:
    rotate_index = x - 1
    dir = 1 if d == 0 else -1
    k %= m
    while rotate_index < n:
        rotateList(rotate_index, dir * k)
        rotate_index += x
    if not check(x-1):
        if cnt == 0:
            break
        else:
            remain = ssum % cnt
            avg = ssum // cnt
            if remain:
                avg += 0.5
            for i in range(n):
                for j in range(m):
                    if li[i][j] == -1:
                        continue
                    if li[i][j] > avg:
                        ssum -= 1
                        li[i][j] -= 1
                    elif li[i][j] < avg:
                        ssum += 1
                        li[i][j] += 1
print(ssum)