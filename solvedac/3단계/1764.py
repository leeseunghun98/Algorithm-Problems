import sys
n, m = map(int, sys.stdin.readline().strip().split())
a = set(sys.stdin.readline().strip() for _ in range(n))
b = set(sys.stdin.readline().strip() for _ in range(m))
c = a.intersection(b)
c = sorted(list(c))
print(len(c))
for i in c:
    print(i)
