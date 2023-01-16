import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
count = Counter(li)
for i in range(n):
    li[i] = (count[li[i]], li[i])
answer = [-1 for _ in range(n)]
queue = []
for i in range(n-1, -1, -1):
    while queue and queue[-1][0] <= li[i][0]:
        queue.pop()
    if queue:
        answer[i] = queue[-1][1]
    queue.append(li[i])
print(*answer)