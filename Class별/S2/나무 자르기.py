import sys
from collections import Counter
input = sys.stdin.readline
n, m = map(int, input().split())
li = Counter(map(int, input().split()))
s = 1
t = max(li)
while s <= t:
    mid = (s+t) // 2

    trees = 0
    for h, c in li.items():
        if h >= mid:
            trees += (h - mid) * c

    if trees >= m:
        s = mid + 1
    else:
        t = mid - 1
print(t)