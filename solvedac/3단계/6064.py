import sys
n = int(sys.stdin.readline())
for _ in range(n):
    N, M, x, y = map(int, sys.stdin.readline().strip().split())
    a = x
    b = y
    if x == 1 and y == 1:
        print(0)
    else:
        while True:
            if x > a + N * M and y > b + N * M:
                x = -1
                break
            elif x == y:
                break
            elif x > y:
                y += M
            else:
                x += N
        print(x)