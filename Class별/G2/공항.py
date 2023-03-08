import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
g, p = int(input()), int(input())
planes = [int(input()) for _ in range(p)]
visited = [i for i in range(g+1)]

def find_under(pos):
    if visited[pos] != pos:
        visited[pos] = find_under(visited[pos])
    return visited[pos]

cnt = 0
for i in planes:
    idx = find_under(i)
    if idx == 0:
        break
    visited[idx] = find_under(visited[idx]-1)
    cnt += 1
print(cnt)