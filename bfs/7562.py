import sys
input = sys.stdin.readline
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
def bfs(x, y, visited, l, fin_x, fin_y):
    visited[x][y] = 1
    queue = [[x, y]]
    cnt = 0
    if x == fin_x and y == fin_y:
        return 0
    while queue:
        lst = []
        for a in queue:
            for i in range(8):
                nx = dx[i] + a[0]
                ny = dy[i] + a[1]
                if (0<=nx<l) and (0<=ny<l) and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    lst.append([nx, ny])
                    if nx == fin_x and ny == fin_y:
                        return cnt + 1
        cnt += 1
        queue = lst  
for _ in range(int(sys.stdin.readline().strip())):
    l = int(sys.stdin.readline().strip())
    stt = list(map(int, input().strip().split()))
    fin = list(map(int, input().strip().split()))
    visited = [[0 for _ in range(l)] for _ in range(l)]
    print(bfs(stt[0], stt[1], visited, l, fin[0], fin[1]))


# import sys
# from collections import deque
# dx = [-2, -2, -1, -1, 1, 1, 2, 2]
# dy = [-1, 1, -2, 2, -2, 2, -1, 1]
# def bfs(x, y, visited, l, fin_x, fin_y):
#     visited[x][y] = 1
#     queue = deque()
#     queue.append([[x, y]])
#     cnt = 0
#     if x == fin_x and y == fin_y:
#         return 0
#     while queue:
#         lst = []
#         j = queue.popleft()
#         for a in j:
#             for i in range(8):
#                 nx = dx[i] + a[0]
#                 ny = dy[i] + a[1]
#                 if (0<=nx<l) and (0<=ny<l) and visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     lst.append([nx, ny])
#                     if nx == fin_x and ny == fin_y:
#                         return cnt + 1
#         cnt += 1
#         queue.append(lst)  
# for _ in range(int(sys.stdin.readline().strip())):
#     l = int(sys.stdin.readline().strip())
#     stt = list(map(int, sys.stdin.readline().strip().split()))
#     fin = list(map(int, sys.stdin.readline().strip().split()))
#     visited = [[0 for _ in range(l)] for _ in range(l)]
#     print(bfs(stt[0], stt[1], visited, l, fin[0], fin[1]))