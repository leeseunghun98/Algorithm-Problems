import sys
import heapq
input = sys.stdin.readline
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
roads = [[] for _ in range(n+1)]
for _ in range(r):
    s, e, t = map(int, input().split())
    roads[s].append((e, t))
    roads[e].append((s, t))

answer = 0
for start in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    queue = [(0, start)]
    ans = 0
    while queue:
        j = heapq.heappop(queue)
        if visited[j[1]] != 0:
            continue
        visited[j[1]] = 1
        ans += items[j[1]]
        for next, cost in roads[j[1]]:
            if visited[next] == 0 and cost + j[0] <= m:
                heapq.heappush(queue, (j[0] + cost, next))
    if answer < ans:
        answer = ans
print(answer)