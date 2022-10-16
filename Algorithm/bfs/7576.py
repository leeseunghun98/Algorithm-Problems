import sys
from collections import deque
m, n = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(m)] for _ in range(n)]
def bfs(start, visited, graph):
    for i in start:
        visited[i[0]][i[1]] = 1
    queue = deque()
    queue.append(start)
    cnt = 1
    while queue:
        cnt += 1
        j = queue.popleft()
        a = []
        for k in j:
            for i in range(4):
                nx = k[0] + dx[i]
                ny = k[1] + dy[i]
                if (0<=nx<n) and (0<=ny<m) and visited[nx][ny] == 0:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = cnt
                        a.append([nx, ny])
                    elif graph[nx][ny] == -1:
                        visited[nx][ny] = -1
        if a != []:
            queue.append(a)
b = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            b.append([i, j])
bfs(b, visited, graph)
result = 0
re = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] > result:
            result = visited[i][j]
        elif visited[i][j] == 0 and graph[i][j] == 0:
            re = 1
            result = 0
            break
    if re == 1:
        break
print(result-1)


# import sys
# from collections import deque
# m, n = map(int, sys.stdin.readline().strip().split())
# graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# result = [[-1 for _ in range(m)] for _ in range(n)]
# def bfs(x, y, visited, graph):
#     visited[x][y] = 1
#     queue = deque([[[x, y, 1]]])
#     while queue:
#         a = []
#         j = queue.popleft()
#         for i in j:
#             for j in range(4):
#                 nx = i[0] + dx[j]
#                 ny = i[1] + dy[j]
#                 if (0<=nx<n) and (0<=ny<m) and visited[nx][ny] == 0:
#                     if graph[nx][ny] == 0:
#                         a.append([nx, ny, i[2] + 1])
#                         visited[nx][ny] = 1
#                     elif graph[nx][ny] == 1:
#                         return i[2]
#         if a != []:
#             queue.append(a)
#     return -1
# result = -1
# b = 0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == -1:
#             continue
#         elif graph[i][j] == 1:
#             a = 0
#         else:
#             visited = [[0 for _ in range(m)] for _ in range(n)]
#             a = bfs(i, j, visited, graph)
#         if a == -1:
#             b = 1
#         elif result < a:
#             result = a
# print(result if b == 0 else -1)