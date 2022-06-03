import sys
import heapq
n = int(sys.stdin.readline().strip())
li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
li.sort(key=lambda x:x[1])
heap = []
for i in li:
    heapq.heappush(heap, i[0])
    if i[1] < len(heap):
        heapq.heappop(heap)
print(sum(heap))