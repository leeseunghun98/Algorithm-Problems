import sys
from collections import deque
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
graph = [0 for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, list(sys.stdin.readline()[:m])))

cnt = 1
start = [[0, 0]]
directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

def find(graph, cnt, nodes):
    a = []
    for node in nodes:
        graph[node[0]][node[1]] = cnt
        for dir in directions:
            if node[0] + dir[0] >= 0 and node[0] + dir[0] <n and node[1] + dir[1] >=0 and node[1] + dir[1] <m:
                if graph[node[0] + dir[0]][node[1] + dir[1]] == 1:
                    if [node[0] + dir[0], node[1] + dir[1]] not in a:
                        a.append([node[0] + dir[0], node[1] + dir[1]])
    if a != []:
        cnt += 1
        find(graph, cnt, a)
        
        
find(graph, cnt, start)
print(graph[n-1][m-1])



