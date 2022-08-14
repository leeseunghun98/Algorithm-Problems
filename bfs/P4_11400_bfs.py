import sys
input = sys.stdin.readline
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
li = []
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    li.append([a, b])
def bfs(lst, start):
    visited = [0 for _ in range(v+1)]
    visited[0] = 1
    visited[start] = 1
    queue = set()
    queue.add(start)
    while queue:
        j = queue.pop()
        for i in lst[j]:
            if visited[i] == 0:
                visited[i] = 1
                queue.add(i)
    for i in visited:
        if i == 0:
            return True
    return False
result = []
for i in li:
    graph[i[0]].remove(i[1])
    graph[i[1]].remove(i[0])
    if bfs(graph, i[0]) == True:
        result.append(i)
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
print(len(result))
for i in result:
    print(*i)