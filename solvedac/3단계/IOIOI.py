import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input().rstrip()
idx = 0
mode = 0
answer = 0
while idx < m:
    if not mode:
        if idx < m-2 and s[idx:idx+3] == 'IOI':
            mode = 1
            idx += 3
            continue
        idx += 1
    else:
        if idx < m-1 and s[idx:idx+2] == 'OI':
            mode += 1
            idx += 2
            continue
        answer += max(0, mode-n+1)
        mode = 0
if mode:
    answer += max(0, mode-n+1)
print(answer)