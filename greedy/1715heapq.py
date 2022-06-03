import heapq
import sys
input = sys.stdin.readline
n = int(input().strip())
li = [int(input().strip()) for _ in range(n)]
heapq.heapify(li)
sum=0
while len(li) > 1:
    a = heapq.heappop(li)
    b = heapq.heappop(li)
    c = a + b
    sum += c
    heapq.heappush(li, c)
print(sum)
