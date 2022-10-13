import sys
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))
ret = set([])
for i in permutations(li, m):
    ret.add(i)
ret = sorted(ret)
for r in ret:
    print(*r)