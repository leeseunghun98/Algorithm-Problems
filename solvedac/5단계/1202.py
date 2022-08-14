import sys
import heapq
n, k = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
li.sort(key=lambda x:x[0])
m = []
for _ in range(k):
    heapq.heappush(m, int(sys.stdin.readline()))
result = 0
while m and li:
    w = heapq.heappop(m)
    mx = 0
    mx_idx = -1
    for i in range(len(li)):
        if li[i][0] <= w and mx < li[i][1]:
            mx = li[i][1]
            mx_idx = i
        elif li[i][0] > w:
            break
    if mx_idx == -1:
        continue
    else:
        li.pop(mx_idx)
        result += mx
print(result)