import sys
import heapq
input = sys.stdin.readline
m, n = map(int, input().split())
li = [list(map(int, list(input().rstrip()))) for _ in range(n)]
boundary_chk = lambda x, y : True if (0<=x<n) and (0<=y<m) else False
dx = (1, 0, 0, -1)
dy = (0, 1, -1, 0)

dp = [[10000 for _ in range(m)] for _ in range(n)]

queue = [(0, 0, 0)]
while queue:
    cnt, x, y = heapq.heappop(queue)
    if x == n-1 and y == m-1:
        print(cnt)
        break

    if dp[x][y] <= cnt:
        continue
    dp[x][y] = cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if boundary_chk(nx, ny):
            if li[nx][ny]:
                if dp[nx][ny] > cnt + 1:
                    heapq.heappush(queue, (cnt+1, nx, ny))
            elif dp[nx][ny] > cnt:
                heapq.heappush(queue, (cnt, nx, ny))