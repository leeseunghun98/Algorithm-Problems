import sys
n, k = map(int, sys.stdin.readline().strip().split())
a = 1
while a*2 < n:
    a *= 2
for i in range(k-1):
    while n <= a:
        a //= 2
    n -= a
a = 1
while n > a:
    a *= 2
print(a-n)