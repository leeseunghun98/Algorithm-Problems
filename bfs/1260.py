import sys
from collections import deque

n, links, start = map(int, sys.stdin.readline().split())
visit = []
for i in range(links):
    visit.append(list(map(int, sys.stdin.readline().split())))

graph = [[] for _ in range(n+1)]

for i in visit:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for i in range(n):
    graph[i+1].sort()
    
v = [False] * (n + 1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, start, v)
print()
v = [False] * (n + 1)
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, start, v)
