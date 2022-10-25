import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
t = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    t[b].append(a)
visited = [0 for _ in range(n+1)]

def dfs(start):
    ret = 1
    visited[start] = -1
    for i in t[start]:
        if not visited[i]:
            ret += dfs(i)
        else:
            ret += visited[i]
    visited[start] = ret
    return ret

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

ans = max(visited)
answer = []
for i in range(1, n+1):
    if visited[i] == ans:
        answer.append(i)
print(*answer)