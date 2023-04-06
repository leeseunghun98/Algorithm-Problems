import sys
import heapq
input = sys.stdin.readline
v, e = map(int, input().split())
roads = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    roads[a].append((c, b))
back = [0 for _ in range(v+1)]
def find(pos):
    queue = [(1, pos)]
    while queue:
        cost, now = heapq.heappop(queue)
        if back[now]:
            continue
        if visited[now]:
            back[now] = cost-visited[now]
            continue
        visited[now] = cost
        for next_cost, next_next in roads[now]:
            heapq.heappush(queue, (cost+next_cost, next_next))

for i in range(1, v+1):
    if not back[i]:
        visited = [0 for _ in range(v+1)]
        find(i)

answer = max(back)
print(answer if answer > 0 else -1)