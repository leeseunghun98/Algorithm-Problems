import sys
from collections import deque
n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    
def bfs(v, dest):
    if v == dest:
        return
    queue = deque()
    queue.append([v, []])
    while queue:
        j = queue.popleft()
        for i in range(4):
            if i == 0:
                
            elif i == 1:
                pass
            elif i == 2:
                pass
            elif i == 3:
                pass

# a = ['1', '0', '0', '0']
# print(int("".join(a)))