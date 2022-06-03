import sys
import copy
n = int(sys.stdin.readline().rstrip('\n'))

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))

maxnum = 0

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs(graph, start):
    if graph[start[0]][start[1]] == 1:
        graph[start[0]][start[1]] = 0
        for di in dir:
            if start[0]+di[0]<0 or start[0]+di[0] >= n or start[1]+di[1]<0 or start[1]+di[1]>=n:
                continue
            if graph[start[0]+di[0]][start[1]+di[1]] == 1:
                dfs(graph, [start[0]+di[0], start[1]+di[1]])
        return True
    return False

max = 0
for i in range(n):
    for j in range(n):
        if max < graph[i][j]:
            max = graph[i][j]
for i in range(max):
    graph2 = copy.deepcopy(graph)
    cnt = 0
    for k in range(n):
        for l in range(n):
            if graph2[k][l] > i:
                graph2[k][l] = 1
            else:
                graph2[k][l] = 0

    for a in range(n):
        for b in range(n):
            if True == dfs(graph2, [a, b]):
                cnt += 1
    if maxnum < cnt:
        maxnum = cnt

print(maxnum)