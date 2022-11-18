import sys
from itertools import combinations
input = sys.stdin.readline
l, c = map(int, input().split())
li = sorted(list(input().split()))

mo = 'aeiou'
for com in combinations(li, l):
    a, b = 0, 0
    ret = 0
    for q in com:
        if q in mo:
            a += 1
        else:
            b += 1
        if a >= 1 and b >= 2:
            ret = 1
            break
    if ret:
        print(''.join(com))