import sys
input = sys.stdin.readline
c, d = map(int, input().split())
a = max(c, d)
b = min(c, d)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a - (a // b) * b)

print('1' * gcd(a, b))