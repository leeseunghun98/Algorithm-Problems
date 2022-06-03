import sys

N, M = map(int, sys.stdin.readline().split())
graph1, graph2 = [], []
for _ in range(N):
    graph1.append(list(map(int, list(sys.stdin.readline().rstrip('\n')))))
for _ in range(N):
    graph2.append(list(map(int, list(sys.stdin.readline().rstrip('\n')))))
cnt = 0
if N > 2 and M > 2:
    for n in range(N-2):
        for m in range(M-2):
            if graph1[n][m] != graph2[n][m]:
                cnt += 1
                for i in range(3):
                    for j in range(3):
                        graph1[n + i][m + j] = 1 - graph1[n + i][m + j]

if graph1 == graph2:
    print(cnt)
else:
    print(-1)