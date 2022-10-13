from operator import mod
import sys
input = sys.stdin.readline
m = int(input())
x, y = 0, 0
for _ in range(m):
    a, b = map(int, input().split())
    x += a
    y += b
bb = 0
for i in range(y):
    if mod(x*i, 1000000007) == 1:
        bb = i
        break
print(mod(x*bb, 1000000007))