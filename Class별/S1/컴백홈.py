import sys
input = sys.stdin.readline
r, c, k = map(int, input().split())
li = [list(input().rstrip()) for _ in range(r)]
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)
boundary_chk = lambda x, y : True if (0<=x<r) and (0<=y<c) else False

visited = [[0 for _ in range(c)] for _ in range(r)]
def dfs(x, y, depth):
    if depth == k:
        if x == 0 and y == c-1:
            return 1
        return 0
    cnt = 0
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if boundary_chk(nx, ny) and not visited[nx][ny] and li[nx][ny] == '.':
            cnt += dfs(nx, ny, depth+1)
    visited[x][y] = 0
    return cnt

print(dfs(r-1, 0, 1))