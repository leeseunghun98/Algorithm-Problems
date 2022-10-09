import sys
import heapq
v, e = map(int, sys.stdin.readline().split())
li = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    li[a].append((b, c))
    li[b].append((a, c))

queue = [(0, 1)]
visited = [0 for _ in range(v+1)]
cnt = 0
answer = 0
while queue:
    j = heapq.heappop(queue)
    if visited[j[1]] != 0:
        continue
    cnt += 1
    answer += j[0]
    if cnt == v:
        print(answer)
        break
    visited[j[1]] = 1
    for i in li[j[1]]:
        if visited[i[0]] == 0:
            heapq.heappush(queue, (i[1], i[0]))