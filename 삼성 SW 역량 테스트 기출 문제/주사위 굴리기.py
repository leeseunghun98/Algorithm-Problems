N, M, x, y, K = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
moving = list(map(int, input().split()))
form = 0
dies = [0, 0, 0, 0, 0, 0, 0]
dx = (0, 0, 0, -1, 1)
dy = (0, 1, -1, 0, 0)
for i in moving:
    if (0 <= x + dx[i] < N) and (0 <= y + dy[i] < M):
        x += dx[i]
        y += dy[i]
        
        if i == 1:
            tmp = dies[4]
            dies[4] = dies[6]
            dies[6] = dies[3]
            dies[3] = dies[1]
            dies[1] = tmp
        elif i == 2:
            tmp = dies[4]
            dies[4] = dies[1]
            dies[1] = dies[3]
            dies[3] = dies[6]
            dies[6] = tmp
        elif i == 3:
            tmp = dies[1]
            dies[1] = dies[5]
            dies[5] = dies[6]
            dies[6] = dies[2]
            dies[2] = tmp
        else:
            tmp = dies[1]
            dies[1] = dies[2]
            dies[2] = dies[6]
            dies[6] = dies[5]
            dies[5] = tmp
        if li[x][y] == 0:
            li[x][y] = dies[6]
        else:
            dies[6] = li[x][y]
            li[x][y] = 0
        print(dies[1])