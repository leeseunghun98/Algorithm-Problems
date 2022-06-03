import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
truth = sys.stdin.readline()
if truth[0] == '0':
    truth = set()
else:
    truth = set(list(map(int, truth.split()))[1:])
truth_ = list(truth)
li = [list(map(int, sys.stdin.readline().split()))[1:] for _ in range(m)]
graph = [set() for _ in range(n+1)]
for i in li:
    for j in i:
        for k in i:
            if j == k:
                pass
            else:
                graph[j].add(k)
def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        j = queue.popleft()
        for i in graph[j]:
            if i not in truth:
                truth.add(i)
                queue.append(i)
for i in truth_:
    bfs(i)
result = m
for i in li:
    for j in i:
        if j in truth:
            result -= 1
            break
print(result)