import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
li = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)
def bfs(start):
    visited[start] = 1
    queue = deque()
    result = 0
    queue.append([start, 0])
    while queue:
        j = queue.popleft()
        a = []
        for i in j[:len(j) - 1]:
            for k in li[i]:
                if visited[k] == 0:
                    a.append(k)
                    visited[k] = 1
        a.append(j[-1] + 1)
        result += (len(a) - 1) * (j[-1] + 1)
        if len(a) > 1:
            queue.append(a)
    return result
visited = [0] * (n+1)
mn = bfs(1)
result = 1
for i in range(1, n):
    visited = [0] * (n+1)
    c = bfs(i)
    if mn > c:
        result = i
        mn = c
print(result)