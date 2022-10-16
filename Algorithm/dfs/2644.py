import sys
n = int(sys.stdin.readline().strip())
a, dst = map(int, sys.stdin.readline().strip().split())
links = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(links)]
li = [[] for _ in range(n+1)]
for i in graph:
    li[i[0]].append(i[1])
    li[i[1]].append(i[0])
visited = [0] * (n+1)
def dfs(start, graph, cnt):
    global result
    visited[start] = 1
    for i in graph[start]:
        if i == dst:
            result = cnt
        elif visited[i] == 0:
            dfs(i, graph, cnt + 1)
result = -1
dfs(a, li, 1)
print(result)