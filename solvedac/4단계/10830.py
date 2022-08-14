import sys
sys.setrecursionlimit(10**6)
n, b = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def mul(li1, li2):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            elem = 0
            for k in range(n):
                elem += li1[i][k] * li2[k][j]
            result[i][j] = elem % 1000
    return result

def solve(lst, q):
    if q == 1:
        for i in range(n):
            for j in range(n):
                lst[i][j] %= 1000
        return lst
    a = solve(lst, q//2)
    if q % 2:
        return mul(mul(a, a), lst)
    else:
        return mul(a, a)
res = solve(li, b)
for i in res:
    print(*i)