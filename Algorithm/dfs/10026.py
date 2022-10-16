import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().rstrip('\n'))
li = []
for _ in range(n):
    li.append(list(sys.stdin.readline().rstrip('\n')))
dis = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def dfs(start, graph, rgb):
    if graph[start[0]][start[1]] == rgb:
        if rgb == 'R' or rgb == 'G':
            graph[start[0]][start[1]] = 1
        elif rgb == 'B':
            graph[start[0]][start[1]] = 2
        else:
            graph[start[0]][start[1]] = 3
        for di in dis:
            if start[0]+di[0] < 0 or start[0] + di[0] >= n or start[1]+di[1] < 0 or start[1]+di[1] >= n:
                continue
            elif graph[start[0]+di[0]][start[1]+di[1]] == rgb:
                dfs([start[0]+di[0],start[1]+di[1]], graph, rgb)
        return True
cnt = 0
for rgb in ['R', 'G', 'B']:
    for i in range(n):
        for j in range(n):
            if dfs([i, j], li, rgb) == True:
                cnt += 1
cntt = 0
for rb in [1, 2]:
    for i in range(n):
        for j in range(n):
            if dfs([i, j], li, rb) == True:
                cntt += 1
print(cnt, cntt)