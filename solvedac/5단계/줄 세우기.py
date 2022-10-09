import sys
n, m = map(int, sys.stdin.readline().split())
li = [0] + [[[], 0] for _ in range(n)] # 하는거, 받는거
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    li[b][1] += 1
    li[a][0].append(b)
queue = set([])
for idx, t in enumerate(li[1:]):
    if t[1] == 0:
        queue.add(idx+1)
while queue:
    j = queue.pop()
    print(j, end=" ")
    for i in li[j][0]:
        li[i][1] -= 1
        if li[i][1] == 0:
            queue.add(i)