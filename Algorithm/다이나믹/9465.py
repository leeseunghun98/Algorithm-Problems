import sys
testcase = int(sys.stdin.readline().strip())
for _ in range(testcase):
    n = int(sys.stdin.readline().strip())
    graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2)]
    if n > 1:
        graph[0][1], graph[1][1] = graph[1][0] + graph[0][1], graph[0][0] + graph[1][1]
    for i in range(2, n):
        graph[0][i] = max(graph[0][i] + graph[1][i-1], graph[0][i] + graph[1][i-2])
        graph[1][i] = max(graph[1][i] + graph[0][i-1] , graph[1][i] + graph[0][i-2])
    print(max(max(graph[0]), max(graph[1])))