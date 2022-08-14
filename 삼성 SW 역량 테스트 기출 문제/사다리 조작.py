import sys
N, M, H = map(int, sys.stdin.readline().split())
rows = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
ladder = [[0 for _ in range(N)] for _ in range(H)]
for i in rows:
    ladder[i[0]-1][i[1]-1] = 1
    ladder[i[0]-1][i[1]] = -1

def goDown(ladder, x, y, line):
    if x == len(ladder):
        if y == line:
            return True
        return False
    if ladder[x][y] == 0:
        return goDown(ladder, x+1, y, line)
    elif ladder[x][y] == 1:
        return goDown(ladder, x+1, y+1, line)
    else:
        return goDown(ladder, x+1, y-1, line)

def chk(ladder):
    for line in range(N):
        if goDown(ladder, 0, line, line) == False:
            return False
    return True

def solve(can, ladder, m, row, idx):
    if m == 0:
        if chk(ladder) == True:
            return True
    else:
        for i in range(idx, len(can) - m + 1):
            a, b = can[i][0], can[i][1]
            if ladder[a][b] == 0 and ladder[a][b+1] == 0:
                ladder[a][b] = 1
                ladder[a][b+1] = -1
                if solve(can, ladder, m - 1, row + [can[i]], i+1):
                    return True
                ladder[a][b] = 0
                ladder[a][b+1] = 0

can = []
for i in range(H):
    for j in range(N-1):
        if ladder[i][j] == 0 and ladder[i][j + 1] == 0:
            can.append((i, j))
re = 0
for i in range(4):
    if solve(can, ladder, i, [], 0):
        print(i)
        re = 1
        break
if re == 0:
    print(-1)