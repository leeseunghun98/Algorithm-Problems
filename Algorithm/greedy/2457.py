import sys
n = int(sys.stdin.readline().strip())
date = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
li = []
for _ in range(n):
    a = list(map(int, sys.stdin.readline().strip().split()))
    li.append([date[a[0]] + a[1], date[a[2]] + a[3]])
li.sort(key=lambda x:x[0])
day = 335
cnt = 0
idx = n
while day > 60:
    temp_cnt = cnt
    for index, i in enumerate(li[:idx]):
        if i[1] >= day:
            day = i[0]
            cnt += 1
            idx = index
            break
    if temp_cnt == cnt:
        cnt = 0
        break
print(cnt)