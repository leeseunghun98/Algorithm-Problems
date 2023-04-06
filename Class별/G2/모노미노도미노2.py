import sys
input = sys.stdin.readline
n = int(input())
li = [tuple(map(int, input().split())) for _ in range(n)]

green = [[0 for _ in range(4)] for _ in range(6)]
blue = [[0 for _ in range(4)] for _ in range(6)]
block = [[], [(0, 0)], [(0, 0), (0, 1)], [(0, 0), (1, 0)]]

score = 0

def fallGreen(green, t, x, y):
    top = 0
    ret = 0
    if t == 2:
        for i in range(3, -1, -1):
            if green[i][y] or green[i][y+1]:
                top = i + 1
                break
    else:
        for i in range(3, -1, -1):
            if green[i][y]:
                top = i + 1
                break

    erase = []
    over = []
    for dx, dy in block[t]:
        nx = top + dx
        ny = y + dy
        green[nx][ny] = 1
        if nx >= 4:
            over.append((nx, ny))
        if sum(green[nx]) == 4:
            ret += 1
            erase.append(nx)
    
    return ret, erase, over

def greenDown(green, down):
    for i in range(4):
        green[i] = [j for j in green[i+down]]
    green[4] = [0, 0, 0, 0]
    green[5] = [0, 0, 0, 0]

def greenturn(green, t, x, y):
    global score
    ret, erase, over = fallGreen(green, t, x, y)
    score += ret
    
    if erase:
        a = len(erase)
        b = min(erase)
        for i in range(b, 4):
            green[i] = [i for i in green[i+a]]
        for o in over:
            green[o[0]][o[1]] = 0

    high = 0
    if 1 in green[5]:
        high = 5
    elif 1 in green[4]:
        high = 4
    if high:
        down = high - 3
        greenDown(green, down)

for t, x, y in li:
    greenturn(green, t, x, y)
    q = 1
    if t == 2:
        q = 3
    elif t == 3:
        q = 2
    greenturn(blue, q, 3-y, x)

ans = 0
for i in green:
    ans += sum(i)
for i in blue:
    ans += sum(i)
print(score)
print(ans)