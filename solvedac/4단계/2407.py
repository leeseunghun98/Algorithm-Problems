import sys
n, m  = map(int, sys.stdin.readline().split())
def fact(a):
    if a == 0:
        return 1
    return a * fact(a-1)
print(fact(n)//(fact(m)*fact(n-m)))