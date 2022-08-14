import sys
A, B, C = map(int, sys.stdin.readline().split())

def solve(a, b):
    if b == 1:
        return a % C
    t = solve(a, b//2)
    if b % 2:
        return (t * t * a) % C
    else:
        return (t * t) % C
print(solve(A, B))