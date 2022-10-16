import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n-1)]
li = [[] for _ in range(n+1)]
for i in graph:
    li[i[0]].append(i[1])
    li[i[1]].append(i[0])
visited = [0] * (n+1)
cnt = 0
def dfs(graph, start, visited):
    global cnt
    cnt += 1
    visited[start] = cnt
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, i, visited)
dfs(li, 1, visited)
for i in range(2, n+1):
    for j in li[i]:
        if visited[j] < visited[i]:
            print(j)
            break