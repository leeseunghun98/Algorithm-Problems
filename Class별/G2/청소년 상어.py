li = []
dic = [0 for _ in range(17)]
dy = (0, -1, -1, -1, 0, 1, 1, 1)
dx = (-1, -1, 0, 1, 1, 1, 0, -1)
boundary = lambda x, y : True if (0<=x<4) and (0<=y<4) else False
for i in range(4):
    row = list(map(int, input().split()))
    for k in range(4):
        row[1 + 2*k] -= 1
    per_row = [list(row[:2]), list(row[2:4]), list(row[4:6]), list(row[6:])]
    for j in range(4):
        dic[per_row[j][0]] = [i, j]
    li.append(per_row)

answer = li[0][0][0]

def dfs(now_sharkPos, now_li, now_dic, score):
    global answer
    if answer < score:
        answer = score
    
    next_dic = [i for i in now_dic]
    next_li = [[i for i in j] for j in now_li]
    for fish in range(1, 17):
        x, y = next_dic[fish]
        if next_li[x][y][0] != fish:
            continue
        for di in range(8):
            dir = (next_li[x][y][1] + di) % 8
            nx = x + dx[dir]
            ny = y + dy[dir]
            if boundary(nx, ny) and next_li[nx][ny][0] != -1:
                changedfish = next_li[nx][ny][0]
                next_dic[fish] = [nx, ny]
                next_dic[changedfish] = [x, y]
                next_li[x][y] = [changedfish, next_li[nx][ny][1]]
                next_li[nx][ny] = [fish, dir]
                break

    shark_dir = next_li[now_sharkPos[0]][now_sharkPos[1]][1]
    nx = now_sharkPos[0] + dx[shark_dir]
    ny = now_sharkPos[1] + dy[shark_dir]
    next_li[now_sharkPos[0]][now_sharkPos[1]] = [0, 0]
    while boundary(nx, ny):
        up = next_li[nx][ny][0]
        if up == 0:
            nx += dx[shark_dir]
            ny += dy[shark_dir]
            continue
        next_li[nx][ny][0] = -1
        dfs([nx, ny], next_li, next_dic, score + up)
        next_li[nx][ny][0] = up

        nx += dx[shark_dir]
        ny += dy[shark_dir]

li[0][0][0] = -1
dfs([0, 0], li, dic, answer)
print(answer)