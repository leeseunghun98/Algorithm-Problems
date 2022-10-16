import sys
from itertools import product
input = sys.stdin.readline
n = int(input())
m = int(input())
broken = set()
if m != 0:
    broken = set(map(int, input().split()))
buttons = set([i for i in range(10)]) - broken
ans = float("INF")
test = 0
for i in range(1, 7):
    for j in product(buttons, repeat = i):
        ret = 0
        for q in range(len(j)):
            ret += j[len(j)-1-q] * 10**q
        if ans > abs(ret - n):
            ans = abs(ret - n)
            test = ret
    if ans == 0:
        break
print(min(ans + len(str(test)), abs(n-100)))