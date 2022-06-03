import sys
n = int(sys.stdin.readline().strip())
li = list(map(int, sys.stdin.readline().strip().split()))
result = 0
idx = 0
a = 0
while idx < n-1:
    cnt = -1
    for i in range(idx+1, n):
        cnt += 1
        if li[idx] < li[i]:
            idx = i
            result = max(result, cnt)
            break
        elif i == n-1:
            a = 1
            result = max(result, cnt+1)
    if a == 1:
        break
print(result)