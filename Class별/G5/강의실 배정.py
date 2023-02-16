import sys
import heapq
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    a, b = map(int, input().split())
    li.append((b, a))
li.sort(key=lambda x : x[1])
heap = [li[0][0]]
for i in li[1:]:
    if heap[0] > i[1]:
        heapq.heappush(heap, i[0])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, i[0])
print(len(heap))