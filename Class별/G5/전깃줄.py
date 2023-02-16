import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
li2 = sorted([tuple(map(int, input().split())) for _ in range(n)])
li = tuple(map(lambda x:x[1], li2))

st = [li[0]]
for i in li[1:]:
    idx = bisect_left(st, i)
    if idx == len(st):
        st.append(i)
    else:
        st[idx] = i
print(n - len(st))