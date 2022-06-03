import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    li = []
    for _ in range(n):
        a, b = input().strip().split()
        b = int(b)
        if a == "I":
            if len(li) == 0:
                li.append(b)
            else:
                for i in range(len(li)):
                    if b < li[i]:
                        li.insert(i, b)
                        break
                    elif i == len(li) - 1:
                        li.append(b)
        else:
            if len(li) > 0:
                if b == -1:
                    li.pop(0)
                else:
                    li.pop()
    if len(li) > 0:
        print(li[-1], li[0])
    else:
        print('EMPTY')