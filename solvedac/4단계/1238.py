import sys
from collections import deque
n, m, x = map(int, sys.stdin.readline().split())
li = [[] for _ in range(n+1)]
for _ in range(m):
    st, dest, ti = map(int, sys.stdin.readline().split())
    li[st].append([dest, ti])
def bfs(start):
    visited = [1000000] * (n+1)
    visited[start] = 0
    queue = deque()
    queue.append([start, 0])
    while queue:
        j = queue.popleft()
        for i in li[j[0]]:
            if j[1] + i[1] < visited[i[0]]:
                visited[i[0]] = j[1] + i[1]
                queue.append([i[0], j[1] + i[1]])
    return visited
result = bfs(x)
for i in range(1, n+1):
    result[i] += bfs(i)[x]
print(max(result[1:]))