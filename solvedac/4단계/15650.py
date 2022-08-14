from itertools import permutations
import sys
n, m = map(int, input().split())
li = sorted(list(map(int, sys.stdin.readline().split())))
for i in permutations(li, m):
    print(*i)