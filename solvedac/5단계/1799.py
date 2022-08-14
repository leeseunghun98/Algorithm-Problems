import sys
n = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
one_lst = []
for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            one_lst.append([i, j])
