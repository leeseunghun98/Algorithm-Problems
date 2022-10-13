import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
li = [[0, []] for _ in range(n+1)]
for _ in range(m):
    a = tuple(map(int, input().split()))[1:]
    for i in range(len(a)-1):
        li[a[i]][1].append(a[i+1])
        li[a[i+1]][0] += 1
starts = []
for idx, i in enumerate(li):
    if i[0] == 0:
        starts.append(idx)
queue = deque(starts)
queue.popleft()
answer = []
while queue:
    j = queue.popleft()
    answer.append(j)
    for i in li[j][1]:
        li[i][0] -= 1
        if li[i][0] == 0:
            queue.append(i)
if len(answer) != n:
    print(0)
else:
    for i in answer:
        print(i)