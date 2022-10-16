import sys
sys.setrecursionlimit(10**6)
K = int(sys.stdin.readline().strip())
def dfs(graph, start, idx):
    global a
    b = graph[start]
    graph[start] = idx
    for i in b:
        if graph[i] != True and graph[i] != False:
            if idx == True:
                dfs(graph, i, False)
            else:
                dfs(graph, i, True)
        elif graph[i] == graph[start]:
            a = 1
e = []
for _ in range(K):
    a = 0
    V, E = map(int, sys.stdin.readline().strip().split())
    li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(E)]
    graph = [[] for _ in range(V+1)]
    if V > 1:
        for i in range(E):
            graph[li[i][0]].append(li[i][1])
            graph[li[i][1]].append(li[i][0])
        for i in range(1, V+1):
            if graph[i] != True and graph[i] != False:
                dfs(graph, i, True)
        e.append(a)
        # print('No' if a == 1 else 'YES')
    else:
        e.append(0)
        # print('YES')
for i in e:
    if i == 1:
        print('NO')
    else:
        print('YES')

# import sys
# sys.setrecursionlimit(10**6)
# K = int(sys.stdin.readline().strip())
# def dfs(graph, visited, start, idx):
#     global a
#     visited[start] = idx
#     for i in graph[start]:
#         if visited[i] == 0:
#             if idx == True:
#                 dfs(graph, visited, i, False)
#             else:
#                 dfs(graph, visited, i, True)
#         elif visited[i] == idx:
#             a = 1
# for _ in range(K):
#     a = 0
#     V, E = map(int, sys.stdin.readline().strip().split())
#     li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(E)]
#     visited = [0] * (V+1)
#     graph = [[] for _ in range(V+1)]
#     for i in range(E):
#         graph[li[i][0]].append(li[i][1])
#         graph[li[i][1]].append(li[i][0])
#     dfs(graph, visited, li[0][0], True)
#     print('No' if a == 1 else 'YES')