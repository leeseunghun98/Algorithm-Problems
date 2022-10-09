# 산 양수, 알칼리 음수
import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
first = 0
last = n-1
answer = float("INF")
answer_f = li[0]
answer_l = li[-1]
while first < last:
    a = li[first] + li[last]
    if abs(a) < answer:
        answer = abs(a)
        answer_f = li[first]
        answer_l = li[last]
    if a >= 0:
        last -= 1
    else:
        first += 1
print(answer_f, answer_l)