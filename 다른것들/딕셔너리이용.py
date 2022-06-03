import sys
s = sys.stdin.readline().strip().upper()
a = set(s)
li = {}
for i in a:
    li[i] = 0
for i in s:
    li[i] += 1
mx = max(li.values())
cnt = 0
for i in li:
    if li[i] == mx:
        cnt += 1
        result = i
        if cnt > 1:
            break
print('?' if cnt > 1 else result)