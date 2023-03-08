import sys
from collections import Counter
from bisect import bisect_left
input = sys.stdin.readline
t = int(input())
n = int(input())
a = [0] + list(map(int, input().split()))
m = int(input())
b = [0] + list(map(int, input().split()))
n += 1
m += 1

for i in range(1, n):
    a[i] += a[i-1]
for i in range(1, m):
    b[i] += b[i-1]

ali = []
bli = []
for i in range(n):
    for j in range(i+1, n):
        ali.append(a[j] - a[i])
for i in range(m):
    for j in range(i+1, m):
        bli.append(b[j] - b[i])
bli_counter = Counter(bli)
bli = sorted(set(bli))
answer = 0
for i in ali:
    target = t - i
    idx = bisect_left(bli, target)
    if idx < len(bli) and bli[idx] == target:
        answer += bli_counter[target]
print(answer)