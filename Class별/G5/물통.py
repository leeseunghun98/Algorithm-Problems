import sys
from collections import deque
input = sys.stdin.readline
a, b, c = map(int, input().split())

visited = [[[0 for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]
visited[0][0][c] = 1
queue = deque([(0, 0, c)])
while queue:
    j = queue.popleft()
    if not visited[0][j[1]][j[0]+j[2]]:
        queue.append((0, j[1], j[0]+j[2]))
        visited[0][j[1]][j[0]+j[2]] = 1
    if not visited[j[0]][0][j[1]+j[2]]:
        queue.append((j[0], 0, j[1]+j[2]))
        visited[j[0]][0][j[1]+j[2]] = 1
    if not visited[max(0, j[0]+j[1]-b)][min(b, j[0]+j[1])][j[2]]:
        queue.append((max(0, j[0]+j[1]-b), min(b, j[0]+j[1]), j[2]))
        visited[max(0, j[0]+j[1]-b)][min(b, j[0]+j[1])][j[2]] = 1
    if not visited[min(a, j[0]+j[1])][max(0, j[0]+j[1]-a)][j[2]]:
        queue.append((min(a, j[0]+j[1]), max(0, j[0]+j[1]-a), j[2]))
        visited[min(a, j[0]+j[1])][max(0, j[0]+j[1]-a)][j[2]] = 1
    if not visited[j[0]][min(b, j[1]+j[2])][max(0, j[1]+j[2]-b)]:
        queue.append((j[0], min(b, j[1]+j[2]), max(0, j[1]+j[2]-b)))
        visited[j[0]][min(b, j[1]+j[2])][max(0, j[1]+j[2]-b)] = 1
    if not visited[min(a, j[0]+j[2])][j[1]][max(0, j[0]+j[2]-a)]:
        queue.append((min(a, j[0]+j[2]), j[1], max(0, j[0]+j[2]-a)))
        visited[min(a, j[0]+j[2])][j[1]][max(0, j[0]+j[2]-a)] = 1
answer = []
for i in range(c+1):
    re = 0
    for x in range(1):
        for y in range(b+1):
            if visited[x][y][i]:
                answer.append(i)
                re = 1
                break
        if re:
            break
print(*sorted(answer))