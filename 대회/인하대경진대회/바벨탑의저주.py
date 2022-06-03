import sys
n = int(sys.stdin.readline())
q = [0] + list(map(int, sys.stdin.readline().strip().split()))
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
li = []
for i in graph:
    w = []
    for j in i:
        w.append(q[j])
    li.append(w)
