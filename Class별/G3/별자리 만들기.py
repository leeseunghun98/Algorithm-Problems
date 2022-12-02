import sys
import math
import heapq
input = sys.stdin.readline

n = int(input())
li = [tuple(map(float, input().split())) for _ in range(n)]
tree = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if tree[i][j]:
            continue
        dist = math.sqrt((li[i][0] - li[j][0])**2 + (li[i][1] - li[j][1])**2)
        tree[i][j] = dist
        tree[j][i] = dist

visited = [0 for _ in range(n)]
heap = [(0, 0)] # 0으로 가는데 거리 0
answer = 0
while heap:
    cost, pos = heapq.heappop(heap)
    if visited[pos]:
        continue
    visited[pos] = 1
    answer += cost

    for i in range(n):
        if not visited[i]:
            heapq.heappush(heap, (tree[pos][i], i))

print(answer)