import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
n, m = map(int, input().split())
li = set(map(int, input().split()))
li = sorted(li)
for i in combinations_with_replacement(li, m):
    print(*i)