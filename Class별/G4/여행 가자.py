import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())

roads = [[] for _ in range(n+1)]
for idx in range(1, n+1):
    li = tuple(map(int, input().split()))
    for i in range(n):
        if li[i]:
            roads[idx].append(i+1)

li = tuple(map(int, input().split()))
visited = [0 for _ in range(n+1)]
queue = deque([li[0]])

while queue:
    j = queue.popleft()
    visited[j] = 1
    for i in roads[j]:
        if visited[i]:
            continue
        queue.append(i)

answer = m
for i in li:
    if visited[i]:
        answer -= 1

print("YES" if answer == 0 else "NO")