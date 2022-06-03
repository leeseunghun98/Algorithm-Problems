import sys
n = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = [0, 0]
def solve(lst):
    sm = 0
    len_ = len(lst) // 2
    for i in lst:
        sm += sum(i)
    if sm == 0:
        result[0] += 1
    elif sm == len(lst) ** 2:
        result[1] += 1
    else:
        a, b, c, d = [], [], [], []
        for i in range(len_):
            a.append(lst[i][:len_])
            b.append(lst[i][len_:])
            c.append(lst[i + len_][:len_])
            d.append(lst[i + len_][len_:])
        solve(a)
        solve(b)
        solve(c)
        solve(d)
solve(li)
print(result[0])
print(result[1])