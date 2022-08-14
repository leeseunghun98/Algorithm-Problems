import sys
import heapq
input = sys.stdin.readline
heap = []
n = int(input())
for _ in range(n):
    m = int(input())
    if m == 0:
        if len(heap) > 0:
            a = heapq.heappop(heap)
            print(a[0] * a[1])
        else:
            print(0)
    else:
        if m < 0:
            heapq.heappush(heap, (-m, -1))
        else:
            heapq.heappush(heap, (m, 1))