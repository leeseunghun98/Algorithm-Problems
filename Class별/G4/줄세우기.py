import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
s = [0]
for _ in range(n):
    num = int(input())
    if s[-1] < num:
        s.append(num)
    idx = bisect_left(s, num)
    s[idx] = num
print(n - len(s) + 1)