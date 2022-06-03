import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().strip().split())
li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
def bfs(x, y, graph):
    global cnt
    lst = set([(x, y)])
    while lst:
        qx, qy = lst.pop()
        for i in range(4):
            nx = dx[i] + qx
            ny = dy[i] + qy
            if (0<=nx<N) and (0<=ny<M) and graph[nx][ny] < graph[qx][qy]:
                if nx == N-1 and ny == M-1:
                    cnt += 1
                else:
                    lst.add((nx, ny))
if N == 1 and M == 1:
    print(1)
else:
    bfs(0, 0, li)
    print(cnt)







# # dfs 시간초과 - 확인용 경로 다나오게했음
# import sys
# sys.setrecursionlimit(10**6)
# N, M = map(int, sys.stdin.readline().strip().split())
# li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# cnt = 0
# aa = []
# def dfs(x, y, graph, a):
#     global cnt
#     for i in range(4):
#         nx = dx[i] + x
#         ny = dy[i] + y
#         if (0<=nx<N) and (0<=ny<M) and graph[nx][ny] < graph[x][y]:
#             if nx == N-1 and ny == M-1:
#                 cnt += 1
#                 b = []
#                 for i in a:
#                     b.append(i)
#                 aa.append(b)
#             else:
#                 a.append([nx, ny])
#                 dfs(nx, ny, graph, a)
#                 a.pop(-1)
# dfs(0, 0, li, [[0, 0]])
# print(aa)
# print(cnt)
