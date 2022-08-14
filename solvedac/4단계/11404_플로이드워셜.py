import sys
import heapq
INF = float('inf')
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
li = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    li[a].append((b, c))

def dik(start):
    visited = [INF for _ in range(n+1)]
    visited[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        j = heapq.heappop(queue)
        if j[0] > visited[j[1]]:
            continue
        for i in li[j[1]]:
            if j[0] + i[1] < visited[i[0]]:
                visited[i[0]] = j[0] + i[1]
                queue.append([j[0] + i[1], i[0]])
    for i in range(n+1):
        if visited[i] == INF:
            visited[i] = 0
    return visited
for i in range(1, n+1):
    print(*dik(i)[1:])