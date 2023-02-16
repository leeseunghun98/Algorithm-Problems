import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
neighbors = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
chk = lambda x, y : True if (0<=x<n) and (0<=y<m) else False
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
ices = 0
starts = []
for i in range(n):
    for j in range(m):
        if li[i][j] == 0:
            for di in range(4):
                nx = i + dx[di]
                ny = j + dy[di]
                if chk(nx, ny):
                    neighbors[nx][ny] += 1
        else:
            ices += 1
            starts.append((i, j))

def dfs(x, y, cnt):
    global next_ices
    li[x][y] -= neighbors[x][y]
    visited[x][y] = cnt
    ret = 1
    if li[x][y] <= 0:
        next_ices -= 1
        ans.append((x, y))
        li[x][y] = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if chk(nx, ny) and visited[nx][ny] != cnt and li[nx][ny] > 0:
            ret += dfs(nx, ny, cnt)
    return ret

cnt = 1
next_ices = ices
answer = 0
while ices > 0:
    ans = []
    while li[starts[-1][0]][starts[-1][1]] == 0:
        starts.pop()
    if dfs(starts[-1][0], starts[-1][1], cnt) < ices:
        answer = cnt-1
        break
    for x, y in ans:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if chk(nx, ny):
                neighbors[nx][ny] += 1
    cnt += 1
    ices = next_ices
print(answer)