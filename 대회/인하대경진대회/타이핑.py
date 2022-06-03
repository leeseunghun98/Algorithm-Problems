import sys
s = sys.stdin.readline().strip()
big = 0
cnt = 0
li = []
result = len(s)
for i in s:
    if big == 0:
        if ord(i) < 91:
            li.append(cnt)
            big = 1
            cnt = 1
        else:
            cnt += 1
    else:
        if ord(i) > 91:
            li.append(cnt)
            big = 0
            cnt = 1
        else:
            cnt += 1
if cnt > 0:
    li.append(cnt)
print(li)
for i in range(1, len(li), 2):
    if li[i] <= 1:
        result += 1
    else:
        result += 2
if ord(s[-1]) < 91 and li[-1] > 1:
    result -= 1
print(result)