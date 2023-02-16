import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
li = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    li[a].append((c, b))
    li[b].append((c, a))
visited = [0 for _ in range(n+1)]
queue = [(0, 1)]
answer = 0
while queue:
    cost, pos = heapq.heappop(queue)
    if visited[pos]:
        continue
    answer += cost
    visited[pos] = 1
    for next in li[pos]:
        if not visited[next[1]]:
            heapq.heappush(queue, next)
print(answer)
