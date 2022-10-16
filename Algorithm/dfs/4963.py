import sys
sys.setrecursionlimit(10**6)
dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def dfs(graph, start):
    if graph[start[0]][start[1]] == 1:
        graph[start[0]][start[1]] = 0
        for di in dir:
            if start[0]+di[0] < 0 or start[0]+di[0] >= n or start[1]+di[1] < 0 or start[1]+di[1] >= m:
                pass
            elif graph[start[0] + di[0]][start[1] + di[1]] == 1:
                dfs(graph, [start[0]+di[0], start[1]+di[1]])
        return True
    return False

m, n = 1, 1

while m != 0 or n != 0:
    m, n = map(int, sys.stdin.readline().rstrip('\n').split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))

    cnt = 0
    for i in range(m):
        for j in range(n):
            if True == dfs(graph, [j, i]):
                cnt += 1
    if m != 0 or n != 0:
        print(cnt)