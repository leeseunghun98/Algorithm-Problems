import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
li = [list(map(int, input().strip().split())) for _ in range(N)]
dx = [0, -1, -1]
dy = [-1, 0, -1]
for i in range(N):
    for j in range(M):
        mx = li[i][j]
        for k in range(3):
            nx = dx[k] + i
            ny = dy[k] + j
            if (0<=nx<N) and (0<=ny<M):
                mx = max(mx, li[nx][ny] + li[i][j])
        li[i][j] = mx
print(li[N-1][M-1])