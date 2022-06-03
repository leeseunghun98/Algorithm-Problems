import sys
sys.setrecursionlimit(10**6)
n, links = map(int, sys.stdin.readline().rstrip('\n').split())
graph = []
for i in range(links):
    graph.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))

road = [[] for _ in range(n+1)]
for link in graph:
    road[link[0]].append(link[1])
    road[link[1]].append(link[0])
    
visited = [False] * (n+1)

def dfs(graph, start, visited):
    if visited[start] == False:
        visited[start] = True
        for i in graph[start]:
            if visited[i] == False:
                dfs(graph, i, visited)
        return True
    else:
        return False

cnt = 0
for i in range(n):
    if True == dfs(road, i+1, visited):
        cnt += 1

print(cnt)