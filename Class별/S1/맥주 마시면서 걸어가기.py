import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    visited = [0 for _ in range(n+2)]
    stores = []
    for idx in range(n+2):
        a, b = tuple(map(int, input().split()))
        stores.append((a, b, idx))
    
    stores_next = [[] for _ in range(n+2)]
    for cnt in range(n+2):
        for idx in range(n+2):
            if cnt == idx:
                continue
            if abs(stores[cnt][0] - stores[idx][0]) + abs(stores[cnt][1] - stores[idx][1]) <= 1000:
                stores_next[cnt].append(idx)

    queue = deque([0])
    fl = 0
    visited[0] = 1
    while queue:
        idx = queue.popleft()
        if stores[idx][0] == stores[-1][0] and stores[idx][1] == stores[-1][1]:
            fl = 1
            break
        for next in stores_next[idx]:
            if visited[next]:
                continue
            visited[next] = 1
            queue.append(next)
        
    print("happy" if fl else "sad")