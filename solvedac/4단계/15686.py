import sys
n, m = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ones = []
twos = []
for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            ones.append([i, j])
        elif li[i][j] == 2:
            twos.append([i, j])
dist = [[] for _ in range(len(twos))]
for i in range(len(twos)):
    for j in range(len(ones)):
        dist[i].append(abs(twos[i][0] - ones[j][0]) + abs(twos[i][1] - ones[j][1]))
print(dist)