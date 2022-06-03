import sys
import heapq
n = int(sys.stdin.readline().strip())
li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
li.sort(key=lambda x:x[0])
queue = []
for i in li:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)
print(sum(queue))