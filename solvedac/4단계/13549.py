import sys
import heapq
n, m = map(int, sys.stdin.readline().split())
def bfs(start):
    visited = [200001 for _ in range(200001)]
    queue = []
    heapq.heappush(queue, [0, start])
    visited[start] = 0
    while queue:
        j = heapq.heappop(queue)
        if j[1] == m:
            return j[0]
        if j[1] < m and j[0] < visited[j[1] * 2]:
            heapq.heappush(queue, [j[0], j[1] * 2])
            visited[j[1] * 2] = j[0]
        if j[0] + 1 < visited[j[1] + 1]:
            heapq.heappush(queue, [j[0] + 1, j[1] + 1])
            visited[j[1] + 1] = j[0] + 1
        if j[1] - 1 >= 0 and j[0] + 1 < visited[j[1] - 1]:
            heapq.heappush(queue, [j[0] + 1, j[1] - 1])
            visited[j[1] - 1] = j[0] + 1
print(bfs(n))