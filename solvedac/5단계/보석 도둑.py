import sys
import heapq
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
jewels = deque(sorted([tuple(map(int, input().split())) for _ in range(n)]))
bags = sorted([int(input()) for _ in range(k)])
j = []
answer = 0
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(j, -jewels.popleft()[1])
    if j:
        answer += heapq.heappop(j)
print(-answer)