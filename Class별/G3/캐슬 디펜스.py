import sys
import heapq
from itertools import combinations
input = sys.stdin.readline

n, m, d = map(int, input().split())
base_li = [list(map(int, input().split())) for _ in range(n)]

base_enemies = [[] for _ in range(m)]

def heappop(lst, turn):
    flag = 0
    while lst and lst[0][0] <= turn:
        _, b, a = heapq.heappop(lst)
        if a + turn - d >= n:
            continue
        if not li[a][b]:
            li[a][b] = turn
            flag = 1
            break
        elif li[a][b] == turn:
            break
    return flag
                       
for i in range(n):
    for j in range(m):
        if base_li[i][j]:
            for a in range(m):
                row = abs(j-a)
                dist = n-i+row
                if row < d:
                    heapq.heappush(base_enemies[a], (dist, j, i))

answer = 0
for a, b, c in combinations(range(m), 3):
    enemies = [[] for _ in range(m)]
    for i in range(m):
        enemies[i] = base_enemies[i][:]
    li = [[0 for _ in range(m)] for _ in range(n)]
    ret = 0
    for turn in range(d, d+n):
        ret += heappop(enemies[a], turn)
        ret += heappop(enemies[b], turn)
        ret += heappop(enemies[c], turn)
    answer = max(answer, ret)

print(answer)






