import sys
from collections import deque
a, b = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(a+b)]
visited = [0] * 100
def bfs():
    queue = deque()
    queue.append([1, 0])
    while queue:
        j = queue.popleft()
        c = []
        for i in j[:-1]:
            for a in range(1, 7):
                if i + a >= 100:
                    return j[-1] + 1
                elif visited[i+a] == 0:
                    q = 0
                    for k in li:
                        if i + a == k[0]:
                            if visited[k[1]] == 0:
                                c.append(k[1])
                                visited[k[0]] = 1
                                visited[k[1]] = 1
                                q = 1
                                break
                            else:
                                visited[k[0]] = 1
                                q = 1
                    if q == 0:
                        c.append(i + a)
                        visited[i+a] = 1
        c.append(j[-1] + 1)
        queue.append(c)
print(bfs())