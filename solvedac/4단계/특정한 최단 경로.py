import sys
import heapq
input = sys.stdin.readline
n, e = map(int, input().split())
roads = [[] for _ in range(n+1)]
for _ in range(e):
    s, e, t = map(int, input().split())
    roads[s].append((e, t))
    roads[e].append((s, t))
v1, v2 = map(int, input().split())

def dijkstra(start, finish):
    queue = [(0, start, (1 << n) + 1)]
    while queue:
        j = heapq.heappop(queue)
        if j[1] == finish:
            return j[0]
        if j[2] == (1 << n+1) - 1:
            return False
        for next, cost in roads[j[1]]:
            if not (j[2] & (1 << (next-1))):
                heapq.heappush(queue, ((j[0]+cost, next, j[2] | 1 << (next-1))))
a, b = dijkstra(1, v1), dijkstra(1, v2)
c = dijkstra(v1, v2)
d, e = dijkstra(v1, n), dijkstra(v2, n)
if (not a and not b) or (not c) or (not d and not e):
    answer = -1
else:
    answer = min(a + c + e, b + c + d)
print(answer)
