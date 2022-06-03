import sys
n = int(sys.stdin.readline())
li = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
def solve(lst):
    len_ = len(lst) // 2
    a = 0
    for i in lst:
        a += sum(i)
    if a == 0:
        print(0, end="")
    elif a == len(lst) ** 2:
        print(1, end="")
    else:
        print("(", end="")
        for i in range(4):
            a = []
            for j in range(len_):
                if i % 2 == 0:
                    k = 0
                else:
                    k = len_
                if i < 2:
                    a.append(lst[j][k:k + len_])
                else:
                    a.append(lst[j + len_][k:k + len_])
            solve(a)
        print(")", end="")
solve(li)