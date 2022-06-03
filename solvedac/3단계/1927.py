import heapq
import sys
heap = []
li = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(heap) == 0:
            li.append(0)
        else:
            li.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, n)
for i in li:
    print(i)