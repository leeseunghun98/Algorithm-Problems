import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(n)]
tasks.sort(key=lambda x:-x[1])
start = tasks[0][1]
queue = deque(tasks)
while queue:
    j = queue.popleft()
    if start >= j[1]:
        start = j[1]-j[0]
    else:
        start -= j[0]
print(start if start >= 0 else -1)