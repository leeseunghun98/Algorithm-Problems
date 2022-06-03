import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
li = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)
def dfs(start):
    visited[start] = 1
    print(start, end=" ")
    for i in sorted(li[start]):
        if visited[i] == 0:
            dfs(i)
def bfs(start):
    visited[start] = 1
    queue = deque()
    queue.append(start)
    while queue:
        j = queue.popleft()
        print(j, end=' ')
        for i in sorted(li[j]):
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
visited = [0] * (n+1)
dfs(v)
print()
visited = [0] * (n+1)
bfs(v)