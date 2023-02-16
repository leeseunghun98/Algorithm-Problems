import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = [tuple(map(int, tuple(input().rstrip()))) for _ in range(n)]
boundary_chk = lambda x, y : True if (0<=x<n) and (0<=y<m) else False
visited = [[0 for _ in range(m)] for _ in range(n)]
starts = [(0, 0)]
cnt = 1
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
visited[0][0] = 1
while True:
    getAnswer = 0
    for x, y in starts:
        visited[x][y] = cnt
        if x == n-1 and y == m-1:
            print(cnt)
            getAnswer = 1
            break
    if getAnswer:
        break
    cnt += 1
    next_starts = set([])
    for x, y in starts:
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if boundary_chk(nx, ny) and not visited[nx][ny] and li[nx][ny]:
                next_starts.add((nx, ny))
    starts = next_starts
