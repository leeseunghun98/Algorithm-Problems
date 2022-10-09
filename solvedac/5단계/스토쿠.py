import sys
fl = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(9)]
c = [[False for _ in range(10)] for _ in range(10)]
c2 = [[False for _ in range(10)] for _ in range(10)]
c3 = [[False for _ in range(10)] for _ in range(10)]
n = 9

def square(x, y):
    return (x // 3) * 3 + (y // 3)

cnt = 0
def go(z):
    global cnt
    if z == 81:
        for i in fl:
            print(*i, sep="")
        return True
    x = z // n
    y = z % n
    if fl[x][y] != 0:
        return go(z+1)
    else:
        for q in range(1, 10):
            if c[x][q] == 0 and c2[y][q] == 0 and c3[square(x, y)][q] == 0:
                fl[x][y] = q
                c[x][q] = c2[y][q] = c3[square(x, y)][q] = True
                if go(z+1):
                    return True
                fl[x][y] = 0
                c[x][q] = c2[y][q] = c3[square(x, y)][q] = False
    return False

for x in range(n):
    for y in range(n):
        if fl[x][y] != 0:
            a = fl[x][y]
            c[x][a] = c2[y][a] = c3[square(x, y)][a] = True

go(0)
