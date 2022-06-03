import sys
import heapq
n = int(sys.stdin.readline())
heap = []
li = []
for _ in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(heap) > 0:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -m)