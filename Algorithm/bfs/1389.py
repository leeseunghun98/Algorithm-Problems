import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
for i in li:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
def bfs(graph, start, visited):
    visited[start[0]] = 1
    cnt = 1
    result = 0
    queue = deque([[graph[start[0]], cnt]])
    while queue:
        j = queue.popleft()
        for i in j[0]:
            if visited[i] == 0:
                visited[i] = 1
                result += j[1]
                queue.append([graph[i], j[1]+1])
    return result
visited = [0] * (N+1)
res = 1
c = bfs(graph, [1], visited)
for i in range(1, N+1):
    visited = [0] * (N+1)
    b = bfs(graph, [i], visited)
    if c > b:
        res = i
        c = b
print(res)