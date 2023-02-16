import sys
input = sys.stdin.readline
n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(pos):
    if pos != parent[pos]:
        parent[pos] = find(parent[pos])
    return parent[pos]

def union(x, y):
    root1 = find(x)
    root2 = find(y)
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2

li = [tuple(map(int, input().split())) for _ in range(m)]
li.sort(key=lambda x:x[2])
mx = 0
total = 0
roads = 0
for a, b, cost in li:
    if roads == n-1:
        break
    if find(a) != find(b):
        union(a, b)
        total += cost
        roads += 1
        if mx < cost:
            mx = cost
print(total - mx)




# li = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     li[a].append((c, b))
#     li[b].append((c, a))

# heap = [(0, 1)]
# visited = [0 for _ in range(n+1)]
# mx = 0
# answer = 0
# while heap:
#     road, pos = heapq.heappop(heap)
#     if visited[pos]:
#         continue
#     visited[pos] = 1
#     answer += road
#     if road > mx:
#         mx = road
#     for next in li[pos]:
#         if not visited[next[1]]:
#             heapq.heappush(heap, next)
# print(answer - mx)