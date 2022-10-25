import sys
input = sys.stdin.readline
n = int(input())
li = [tuple(map(int ,input().split())) for _ in range(n)]
li.sort()
mx_floor = 0
for i in li:
    if mx_floor < i[-1]:
        mx_floor = i[-1]
floor = [0 for _ in range(mx_floor)]
answer = 0
for h, s, f in li:
    answer += h - floor[s]
    answer += h - floor[f-1]
    for i in range(s, f):
        floor[i] = h

print(answer)