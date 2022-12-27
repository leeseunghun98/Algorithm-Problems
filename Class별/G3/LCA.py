import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())

def dfs(cur, layer):
    visited[cur] = True
    layers[cur] = layer
    for i in wholetree[cur]:
        if not visited[i]:
            ancestor[i] = cur
            dfs(i, layer+1)

def LCA(s, v):
    a, b = s, v
    if a > b:
        a, b = b, a
    
    if (a, b) in results:
        return results[(a, b)]
    
    while layers[a] != layers[b]:
        if layers[a] > layers[b]:
            a = ancestor[a]
        else:
            b = ancestor[b]
    while a != b:
        a = ancestor[a]
        b = ancestor[b]
    
    results[(s, v)] = a
    return a

ancestor = [0 for _ in range(n+1)]
wholetree = [[] for _ in range(n+1)]
layers = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
results = {}

for _ in range(n-1):
    a, b = map(int, input().split())
    wholetree[a].append(b)
    wholetree[b].append(a)

dfs(1, 0)
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(LCA(a, b))
