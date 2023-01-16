import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
cur_ID = 1
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
r_graph = [[] for _ in range(v+1)]
for _ in range(e):
    s, f = map(int, input().split())
    graph[s].append(f)
    r_graph[f].append(s)

def dfs(pos):
    visited[pos] = 1
    for next in graph[pos]:
        if visited[next]:
            continue
        dfs(next)
    stack.append(pos)

def r_dfs(pos):
    r_visited[pos] = 1
    li.append(pos)
    for next in r_graph[pos]:
        if r_visited[next]:
            continue
        r_dfs(next)

stack = []
visited = [0 for _ in range(v+1)]
for i in range(1, v+1):
    if visited[i]:
        continue
    dfs(i)

answer = []
r_visited = [0 for _ in range(v+1)]
while stack:
    j = stack.pop()
    if r_visited[j]:
        continue
    li = []
    r_dfs(j)
    answer.append(sorted(li))

print(len(answer))
for i in sorted(answer):
    print(*i, -1)




# 8 14
# 1 2
# 2 3
# 3 4
# 4 3
# 4 8
# 8 8
# 3 7
# 7 6
# 6 7
# 7 8
# 2 5
# 2 6
# 5 1
# 5 6

# 7 10
# 1 2
# 2 3
# 3 4
# 4 2
# 2 5
# 5 2
# 5 6
# 6 5
# 6 7
# 7 6

# 4 3
# 1 2
# 3 2
# 4 2