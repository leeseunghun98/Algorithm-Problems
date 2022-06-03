import sys
sys.setrecursionlimit(10**6)
M, N, K = map(int, sys.stdin.readline().rstrip('\n').split())
graph1 = []
graph = [[1 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    graph1.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))
for i in graph1:
    for a in range(i[0], i[2]):
        for b in range(i[1], i[3]):
            graph[M - b - 1][a] = 0
            
direc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def dfs(start, graph, cnt):
    if graph[start[0]][start[1]] == 1:
        graph[start[0]][start[1]] = 0
        cnt.append(1)
        for di in direc:
            if start[0] + di[0] < 0 or start[0] + di[0] >= M or start[1] + di[1] < 0 or start[1] + di[1] >= N:
                continue
            elif graph[start[0] + di[0]][start[1] + di[1]] == 1:
                dfs([start[0] + di[0], start[1] + di[1]], graph, cnt)
        return cnt
    return False

li = []
for i in range(M):
    for j in range(N):
        cc = dfs([i, j], graph, [])
        if cc != False:
            li.append(len(cc))
print(len(li))
li.sort()
for i in li:
    print(i, end=" ")