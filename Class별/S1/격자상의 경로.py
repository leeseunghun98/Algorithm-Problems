import sys
import math
input = sys.stdin.readline
n, m, k = map(int, input().split())

target = (0, 0)
if k != 0:
    target = ((k-1)//m, (k-1)%m)

def cal_comb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)

answer = cal_comb(target[0] + target[1], target[0])
answer *= cal_comb(n-1-target[0] + m-1-target[1], n-1-target[0])
print(answer)
