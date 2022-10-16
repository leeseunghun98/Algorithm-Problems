import sys
n = int(sys.stdin.readline().rstrip('\n'))
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))
f = li
for idx, i in enumerate(li):
    if idx == 0:
        continue
    if idx == 1:
        f[idx][0] += f[0][0]
        f[idx][1] += f[0][0]
    else:
        for index, j in enumerate(i):
            if index == 0:
                f[idx][0] += f[idx-1][0]
            elif index == idx:
                f[idx][idx] += f[idx-1][idx-1]
            else:
                f[idx][index] += max(f[idx-1][index], f[idx-1][index-1])
print(max(f[-1]))