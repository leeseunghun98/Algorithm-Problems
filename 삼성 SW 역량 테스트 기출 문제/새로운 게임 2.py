N, K = map(int, input().split())
li = [tuple(map(int, input().split())) for _ in range(N)]
horses = [list(map(int, input().split())) for _ in range(K)]
for i in range(K):
    horses[i] = [horses[i][0]-1, horses[i][1]-1, horses[i][2]-1]
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
now = [[[] for _ in range(N)] for _ in range(N)]
for idx, horse in enumerate(horses):
    now[horse[0]][horse[1]].append(idx)
def move(lst, horse_number, horse, depth):
    x = horse[0] + dx[horse[2]]
    y = horse[1] + dy[horse[2]]
    if depth == 1:
        if x < 0 or x >= N or y < 0 or y >= N or lst[x][y] == 2:
            return False
    if x < 0 or x >= N or y < 0 or y >= N or lst[x][y] == 2:
        if horse[2] == 0:
            dir = 1
        elif horse[2] == 1:
            dir = 0
        elif horse[2] == 2:
            dir = 3
        else:
            dir = 2
        horses[horse_number] = [horse[0], horse[1], dir]
        return move(lst, horse_number, horses[horse_number], 1)
    else:
        if lst[x][y] == 0:
            re = 0
            for idx, i in enumerate(now[horse[0]][horse[1]]):
                if i == horse_number:
                    re = idx
            for i in now[horse[0]][horse[1]][re:]:
                now[x][y].append(i)
                horses[i] = [x, y, horses[i][2]]
            now[horse[0]][horse[1]] = now[horse[0]][horse[1]][:re]
            horses[horse_number] = [x, y, horse[2]]
            if len(now[x][y]) > 3:
                return True
        else:
            re = 0
            for idx, i in enumerate(now[horse[0]][horse[1]]):
                if i == horse_number:
                    re = idx
            a = []
            for i in now[horse[0]][horse[1]][re:]:
                a.append(i)
                horses[i] = [x, y, horses[i][2]]
            for i in reversed(a):
                now[x][y].append(i)
            now[horse[0]][horse[1]] = now[horse[0]][horse[1]][:re]
            horses[horse_number] = [x, y, horse[2]]
            if len(now[x][y]) > 3:
                return True
    return False
        
answer = 0
ans = 0
while True:
    answer += 1
    for idx, horse in enumerate(horses):
        if move(li, idx, horse, 0):
            ans = 1
            break
    if ans == 1:
        break
    if answer >= 1000:
        answer = -1
        break
print(answer)
