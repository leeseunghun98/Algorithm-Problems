import sys
import heapq
input = sys.stdin.readline
heap = []
n = int(input())
li = []
for _ in range(n):
    m = int(input())
    if m == 0:
        if len(heap) > 0:
            a = heapq.heappop(heap)
            li.append(a[0] * a[1])
            print(a)
        else:
            print(0)
            li.append(0)
    else:
        if m < 0:
            heapq.heappush(heap, (-m, -1))
        else:
            heapq.heappush(heap, (m, 1))
print(li)