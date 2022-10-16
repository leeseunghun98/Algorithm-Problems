import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input().strip())
li = [list(map(int, input().strip().split())) for _ in range(n-1)]
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    graph[li[i][0]].append([li[i][1], li[i][2]])
    graph[li[i][1]].append([li[i][0], li[i][2]])
def dfs(start, graph, distance, prev):
    global res
    global pos
    res = max(res, distance)
    if res == distance:
        pos = start
    for i in graph[start]:
        if i[0] != prev:
            dfs(i[0], graph, distance + i[1], start)
re = 0
pos = 1
for i in range(2):
    res = 0
    dfs(pos, graph, 0, 0)
    re = max(re, res)
print(re)