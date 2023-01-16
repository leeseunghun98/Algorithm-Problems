import sys
import heapq
input = sys.stdin.readline

n = int(input())
a, b, c = [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)]
for i in range(n):
    q, w, e = map(int, input().split())
    a[i] = (q, i)
    b[i] = (w, i)
    c[i] = (e, i)
a.sort()
b.sort()
c.sort()

li = []
test = (a, b, c)
for arr in test:
    for i in range(n-1):
        li.append((abs(arr[i][0] - arr[i+1][0]), arr[i][1], arr[i+1][1]))

tree = [[] for _ in range(n)]
for dist, q, w in li:
    heapq.heappush(tree[q], (dist, w))
    heapq.heappush(tree[w], (dist, q))

visited = [0 for _ in range(n)]
queue = [(0, 0)]
answer = 0
while queue:
    cost, pos = heapq.heappop(queue)
    if visited[pos]:
        continue
    visited[pos] = 1
    answer += cost
    for next in tree[pos]:
        if visited[next[1]]:
            continue
        heapq.heappush(queue, next)

print(answer)