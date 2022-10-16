import sys
from collections import deque
input = sys.stdin.readline
testcase = int(input())
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

for _ in range(testcase):
    n, m = list(map(int, input().split()))
    rooms = [list(input().rstrip()) for _ in range(n)]
    key = list(input().rstrip())

    keys = {}
    needkey = {}
    for room in rooms:
        for r in room:
            keys[r.upper()] = False
            needkey[r.upper()] = []
    for p in ['$', '*', '.']:
        if p in needkey.keys():
            del needkey[p]
    keys['.'] = True
    keys['$'] = True
    for k in key:
        keys[k.upper()] = True

    starts = []
    for i in range(n):
        for j in range(m):
            if (i == 0 or i == n-1 or j == 0 or j == m-1) and (rooms[i][j] == '.' or rooms[i][j] == '$' or rooms[i][j].isalpha()):
                starts.append((i, j))

    queue = deque(starts)
    answer = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for start in starts:
        visited[start[0]][start[1]] = 1
    while queue:
        x, y = queue.popleft()
        now = rooms[x][y]
        if now == '$':
            answer += 1
        elif now.isalpha():
            if now.isupper():
                if not keys[now]:
                    needkey[now].append((x, y))
                    continue
            else:
                up = now.upper()
                keys[up] = True
                for need in needkey[up]:
                    queue.append(need)
                needkey[up] = []

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if (0<=nx<n) and (0<=ny<m) and visited[nx][ny] == 0 and rooms[nx][ny] != '*':
                visited[nx][ny] = 1
                queue.append((nx, ny))

    print(answer)