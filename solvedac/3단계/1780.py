import sys
n = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
result = [0, 0, 0]
def solve(lst):
    len_ = len(lst) ** 2
    a = [0, 0, 0]
    for i in lst:
        for j in i:
            if j == -1:
                a[0] += 1
            elif j == 0:
                a[1] += 1
            else:
                a[2] += 1
    if a[0] == len_:
        result[0] += 1
    elif a[1] == len_:
        result[1] += 1
    elif a[2] == len_:
        result[2] += 1
    else:
        for i in range(3):
            b = lst[i * (len(lst) // 3) : (i + 1) * (len(lst) // 3)]
            for q in range(3):
                c = []
                for k in b:
                    c.append(k[q * len(b): (q + 1) * len(b)])
                solve(c)
solve(li)
for i in result:
    print(i)