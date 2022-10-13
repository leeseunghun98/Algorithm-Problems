import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
buses = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    buses[s].append((e, t))
start, finish = map(int, input().split())

visited = [-1 for _ in range(n+1)]
queue = [(0, start, start)]
while queue:
    now_cost, now_pos, from_pos = heapq.heappop(queue)
    if now_pos == finish:
        visited[now_pos] = from_pos
        print(now_cost)
        break
    if visited[now_pos] != -1:
        continue
    visited[now_pos] = from_pos
    for bus in buses[now_pos]:
        if visited[bus[0]] == -1:
            heapq.heappush(queue, (now_cost + bus[1], bus[0], now_pos))
a = finish
ans = []
while a != start:
    ans.append(a)
    a = visited[a]
ans.append(start)
print(len(ans))
print(*reversed(ans))