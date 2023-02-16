import sys
import heapq
input = sys.stdin.readline
n = int(input())
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
problem_cnt = 1
while n:
    chk = lambda x, y: True if (0<=x<n) and (0<=y<n) else False
    li = [tuple(map(int, input().split())) for _ in range(n)]
    queue = [(0, 0, 0)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    while queue:
        cost, x, y = heapq.heappop(queue)
        if visited[x][y]:
            continue
        if x == n-1 and y == n-1:
            answer = cost
            break
        visited[x][y] = 1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if chk(nx, ny) and not visited[nx][ny]:
                heapq.heappush(queue, (cost+li[nx][ny], nx, ny))
    print("Problem " + str(problem_cnt) + ": " + str(answer + li[0][0]))
    problem_cnt += 1
    n = int(input())
