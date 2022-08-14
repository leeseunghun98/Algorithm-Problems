from collections import deque
N = int(input())
K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
li = []
for _ in range(L):
    a, b = input().split()
    a = int(a)
    li.append((a, b))
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
dir = 0
# 동, 남, 서, 북
snake = [[0 for _ in range(N+1)] for _ in range(N+1)]
for x, y in apples:
    snake[x][y] = 2
snake[1][1] = 1
cnt = 0
head_pos = [1, 1]
tail = deque([(1, 1)])
while True:
    head_pos[0] += dx[dir]
    head_pos[1] += dy[dir]
    if head_pos[0] < 1 or head_pos[0] > N or head_pos[1] < 1 or head_pos[1] > N or snake[head_pos[0]][head_pos[1]] == 1:
        print(cnt + 1)
        break
    if snake[head_pos[0]][head_pos[1]] == 0:
        tails = tail.popleft()
        snake[tails[0]][tails[1]] = 0
    tail.append((head_pos[0], head_pos[1]))
    snake[head_pos[0]][head_pos[1]] = 1
    cnt += 1
    if li and cnt == li[0][0]:
        if li[0][1] == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
        li.pop(0)