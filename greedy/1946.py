import sys
for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    li.sort(key=lambda x:x[0])
    result = 0
    mn = li[0][1]
    for i in range(1, n):
        if li[i][1] > mn:
            result += 1
        else:
            mn = li[i][1]
    print(n - result)