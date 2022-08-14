import sys
from collections import deque
n = int(sys.stdin.readline())
li = [[] for _ in range(n+1)]
for _ in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(s) - 2, 2):
        li[s[0]].append((s[i], s[i + 1]))
        
def bfs(x):
    visited = [0] * (n+1)
    mx = [0, 0]
    visited[x] = 1
    queue = deque()
    queue.append([x, 0])
    
    while queue:
        j = queue.popleft()
        for a, b in li[j[0]]:
            if visited[a] == 0:
                visited[a] = 1
                queue.append([a, j[1] + b])
                
                if mx[1] < j[1] + b:
                    mx = [a, j[1] + b]
    return mx

a = bfs(1)
print(bfs(a[0])[1])


##########################################################

"""
import sys
from collections import deque
n = int(sys.stdin.readline())
li = [[]] + [list(map(int, sys.stdin.readline().split()))[1:-1] for _ in range(n)]
def bfs(x):
    visited = [0] * (n+1)
    mx = [0, 0]
    visited[x] = 1
    queue = deque()
    queue.append([x, 0])
    
    while queue:
        j = queue.popleft()
        for i in range(0, len(li[j[0]]) - 1, 2):
            
            if visited[li[j[0]][i]] == 0:
                visited[li[j[0]][i]] = 1
                queue.append([li[j[0]][i], j[1] + li[j[0]][i+1]])
                
                if mx[1] < j[1] + li[j[0]][i+1]:
                    mx = [li[j[0]][i], j[1] + li[j[0]][i+1]]
    return mx

a = bfs(1)
print(bfs(a[0])[1])
"""