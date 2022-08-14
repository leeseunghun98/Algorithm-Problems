n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
blocks = []
for i in range(n):
    for j in range(m):
        if (0 < li[i][j] < 6):
            cctvs.append((i, j, li[i][j]))
        elif li[i][j] == 6:
            blocks.append((i, j))

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
two = ((0, 2), (1, 3))
three = ((1, 2), (2, 3), (3, 0), (0, 1))
four = ((0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1))
five = (0, 1, 2, 3)
answer = float('inf')

visited = [[0 for _ in range(m)] for _ in range(n)]
for block in blocks:
    visited[block[0]][block[1]] = -1
def solve(visited, lst, cctvs, depth):
    global answer
    if depth == len(cctvs):
        re = 0
        for i in visited:
            for j in i:
                if j == 0:
                    re += 1
        if re < answer:
            answer = re
        return
    if cctvs[depth][2] == 1:
        visited[cctvs[depth][0]][cctvs[depth][1]] += 1
        for i in range(4):
            a = []
            nx = cctvs[depth][0] + dx[i]
            ny = cctvs[depth][1] + dy[i]
            while (0 <= nx < n) and (0 <= ny < m) and lst[nx][ny] < 6:
                visited[nx][ny] += 1
                a.append((nx, ny))
                nx += dx[i]
                ny += dy[i]
            solve(visited, lst, cctvs, depth+1)
            for j in a:
                visited[j[0]][j[1]] -= 1
        visited[cctvs[depth][0]][cctvs[depth][1]] -= 1
        
        
    elif cctvs[depth][2] == 2:
        visited[cctvs[depth][0]][cctvs[depth][1]] += 1
        for i in two:
            a = []
            for j in i:
                nx = cctvs[depth][0] + dx[j]
                ny = cctvs[depth][1] + dy[j]
                while (0 <= nx < n) and (0 <= ny < m) and lst[nx][ny] < 6:
                    visited[nx][ny] += 1
                    a.append((nx, ny))
                    nx += dx[j]
                    ny += dy[j]
            solve(visited, lst, cctvs, depth+1)
            for j in a:
                visited[j[0]][j[1]] -= 1
        visited[cctvs[depth][0]][cctvs[depth][1]] -= 1
        
    elif cctvs[depth][2] == 3:
        visited[cctvs[depth][0]][cctvs[depth][1]] += 1
        for i in three:
            a = []
            for j in i:
                nx = cctvs[depth][0] + dx[j]
                ny = cctvs[depth][1] + dy[j]
                while (0 <= nx < n) and (0 <= ny < m) and lst[nx][ny] < 6:
                    visited[nx][ny] += 1
                    a.append((nx, ny))
                    nx += dx[j]
                    ny += dy[j]
            solve(visited, lst, cctvs, depth+1)
            for j in a:
                visited[j[0]][j[1]] -= 1
        visited[cctvs[depth][0]][cctvs[depth][1]] -= 1
                
    elif cctvs[depth][2] == 4:
        visited[cctvs[depth][0]][cctvs[depth][1]] += 1
        for i in four:
            a = []
            for j in i:
                nx = cctvs[depth][0] + dx[j]
                ny = cctvs[depth][1] + dy[j]
                while (0 <= nx < n) and (0 <= ny < m) and lst[nx][ny] < 6:
                    visited[nx][ny] += 1
                    a.append((nx, ny))
                    nx += dx[j]
                    ny += dy[j]
            solve(visited, lst, cctvs, depth+1)
            for j in a:
                visited[j[0]][j[1]] -= 1
        visited[cctvs[depth][0]][cctvs[depth][1]] -= 1
                
    elif cctvs[depth][2] == 5:
        visited[cctvs[depth][0]][cctvs[depth][1]] += 1
        for j in five:
            a = []
            nx = cctvs[depth][0] + dx[j]
            ny = cctvs[depth][1] + dy[j]
            while (0 <= nx < n) and (0 <= ny < m) and lst[nx][ny] < 6:
                visited[nx][ny] += 1
                a.append((nx, ny))
                nx += dx[j]
                ny += dy[j]
        solve(visited, lst, cctvs, depth+1)
        for j in a:
            visited[j[0]][j[1]] -= 1
        visited[cctvs[depth][0]][cctvs[depth][1]] -= 1

solve(visited, li, cctvs, 0)
print(answer)