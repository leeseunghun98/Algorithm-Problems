import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)
visited = [0 for _ in range(n)]

def dfs(pos, depth):
    visited[pos] = 1
    if depth >= 4:
        return 1
    for next in li[pos]:
        if not visited[next]:
            if dfs(next, depth+1):
                return 1
    visited[pos] = 0
    return 0

answer = 0
for i in range(n):
    if dfs(i, 0):
        answer = 1
        break
print(answer)