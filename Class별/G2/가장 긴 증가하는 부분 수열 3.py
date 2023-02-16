import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
li = tuple(map(int, input().split()))
st = []
for i in li:
    idx = bisect_left(st, i)
    if idx == len(st):
        st.append(i)
    else:
        st[idx] = i
print(len(st))