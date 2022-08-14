import sys
N, L, R = map(int, sys.stdin.readline().split())
countries = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
visited = [[-1 for _ in range(N)] for _ in range(N)]
def bfs(lst, x, y, visited, cnt):
    visited[x][y] = cnt
    queue = set([(x, y)])
    a = []
    b = 0
    while queue:
        j = queue.pop()
        b += lst[j[0]][j[1]]
        a.append(j)
        for i in range(4):
            nx = j[0] + dx[i]
            ny = j[1] + dy[i]
            if (0<=nx<N) and (0<=ny<N) and visited[nx][ny] < cnt and (L <= abs(lst[j[0]][j[1]] - lst[nx][ny]) <= R):
                queue.add((nx, ny))
                visited[nx][ny] = cnt
    res = b // len(a)
    for i in a:
        lst[i[0]][i[1]] = res
    if b > lst[x][y]:
        return True
    return False
cnt = 0
answer = 0
def move(cnt):
    re = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] < cnt:
                if bfs(countries, i, j, visited, cnt):
                    re = 1
    if re == 1:
        return True
    else:
        return False
while move(cnt):
    answer += 1
    cnt += 1

print(answer)