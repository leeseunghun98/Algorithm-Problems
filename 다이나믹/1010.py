from itertools import combinations
import sys
sys.setrecursionlimit(10**6)
testcase = int(sys.stdin.readline().strip())
def fact(n):
    if n == 0: return 1
    return n * fact(n-1)
for _ in range(testcase):
    N, M = map(int, sys.stdin.readline().strip().split())
    a = fact(M) // fact(M-N)
    b = fact(N)
    print(int(a / b))