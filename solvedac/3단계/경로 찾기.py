import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
roads = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            roads[i].append(j)

def bfs(start):
    visited = [0 for _ in range(n)]
    queue = deque([start])
    while queue:
        j = queue.popleft()
        for i in roads[j]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
    return visited

for i in range(n):
    print(*bfs(i))