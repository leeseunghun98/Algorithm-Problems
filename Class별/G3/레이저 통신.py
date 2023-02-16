import sys
input = sys.stdin.readline
m, n = map(int, input().split())
chk = lambda x, y : True if (0<=x<n) and (0<=y<m) else False
li = [tuple(input().rstrip()) for _ in range(n)]
c = []
dx, dy = (-1, 1, 0, 0), (0, 0 ,-1, 1)
for x in range(n):
    for y in range(m):
        if li[x][y] == 'C':
            c.append((x, y))
finish = c[1]

visited = [[0 for _ in range(m)] for _ in range(n)]
next = [c[0]]
visited[c[0][0]][c[0][1]] = 1
cnt = 1
out = 0
while next and not out:
    next_next = []
    while next and not out:
        j = next.pop()
        for i in range(4):
            nx = j[0] + dx[i]
            ny = j[1] + dy[i]
            while chk(nx, ny) and not li[nx][ny] == '*':
                if not visited[nx][ny]:
                    next_next.append((nx, ny))
                    visited[nx][ny] = cnt
                    if nx == finish[0] and ny == finish[1]:
                        out = 1
                        break
                elif visited[nx][ny] != cnt:
                    break
                nx += dx[i]
                ny += dy[i]
            if out:
                break
    next = next_next
    cnt += 1

print(visited[finish[0]][finish[1]] - 1)