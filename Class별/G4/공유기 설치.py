import sys
from bisect import bisect_left
input = sys.stdin.readline

n, c = map(int, input().split())
li = sorted(list(int(input()) for _ in range(n)))

mx = max(li) // (c-1)
first = 0
finish = mx
mid = (first + finish) // 2
while True:
    idx = 0
    cur_mid = mid
    for _ in range(c-1):
        idx = bisect_left(li, li[idx] + mid)
        if idx == n:
            break
    if idx == n:
        finish = mid - 1
    else:
        first = mid + 1
    mid = (first + finish) // 2
    if mid == cur_mid:
        break
print(mid)