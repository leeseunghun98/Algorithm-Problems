import sys
from collections import deque
input = sys.stdin.readline
n, l = map(int, input().split())
li = tuple(map(int, input().split()))

queue = deque([])
for i in range(n):
    if queue and (queue[0][1] < i-l+1):
        del queue[0]
    while queue and (queue[-1][0] >= li[i] or queue[-1][1] < i-l+1):
        del queue[-1]
    queue.append((li[i], i))
        
    print(queue[0][0], end=" ")