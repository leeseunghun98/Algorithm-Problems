import sys
input = sys.stdin.readline
l, r = input().split()

answer = 0
if len(l) == len(r):
    idx = 0
    while idx < len(r):
        if l[idx] == r[idx]:
            if l[idx] == '8':
                answer += 1
            idx += 1
        else:
            break
print(answer)