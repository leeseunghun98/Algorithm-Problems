import sys
input = sys.stdin.readline
r, c = map(int, input().split())
x, y, dx, dy = map(int, input().split())

def gcd(a, b): # a >= b
    if a % b == 0:
        return b
    tmp = b
    b = a % b
    a = tmp
    return gcd(a, b)

if dx == 0 or dy == 0:
    if dx == 0:
        dy = 1
    else:
        dx = 1
else:
    if dx >= dy:
        a = gcd(dx, dy)
    else:
        a = gcd(dy, dx)
    dx //= a
    dy //= a


def dist(a, b):
    return (r - a)**2 + (c - b)**2

cur_dist = dist(x, y)
next_dist = dist(x + dx, y + dy)

while cur_dist > next_dist:
    x += dx
    y += dy
    cur_dist = next_dist
    next_dist = dist(x + dx, y + dy)

print(x, y)