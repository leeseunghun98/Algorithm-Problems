import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n, m = map(int, input().split())
t = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    t[b].append(a)
visited = [0 for _ in range(n+1)]

# SCC

def dfs(pos):
    if visited[pos] > 0:
        return visited[pos]
    if visited[pos] == -1:
        return 0
    ret = 1
    visited[pos] = -1
    for next in t[pos]:
        ret += dfs(next)
    visited[pos] = ret
    return ret

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
answer = max(visited)
for i in range(1, n+1):
    if answer == visited[i]:
        print(i, end=" ")