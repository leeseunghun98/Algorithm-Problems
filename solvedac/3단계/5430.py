import sys
input = sys.stdin.readline
for _ in range(int(input())):
    err = 0
    func = list(input().strip())
    n = int(input())
    a = input().rstrip()[1:-1]
    if len(a) > 0:
        lst = list(map(int, a.split(",")))
    else:
        lst = []
    idx = 0
    for i in func:
        if i == "R":
            if idx == 0:
                idx = -1
            else:
                idx = 0
        elif len(lst) == 0:
            err = 1
            break
        else:
            lst.pop(idx)
    if err == 1:
        print("error")
    else:
        if len(lst) > 0:
            print("[", end="")
        else:
            print("[]")
        if idx == 0:
            for i in range(len(lst)):
                if i == len(lst) - 1:
                    print(lst[i], end="]\n")
                else:
                    print(lst[i], end=",")
        else:
            for i in range(len(lst) - 1, -1, -1):
                if i == 0:
                    print(lst[i], end="]\n")
                else:
                    print(lst[i], end=",")