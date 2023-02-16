import sys
from bisect import bisect_left
input = sys.stdin.readline
n, m = map(int, input().split())
li = list(map(int, input().split()))
for i in range(1, n):
    li[i] += li[i-1]
a = li[-1] // m

