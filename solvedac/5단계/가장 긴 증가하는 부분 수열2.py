import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
li = tuple(map(int, input().split()))
ans = [li[0]]
for i in li[1:]:
    if ans[-1] < i:
        ans.append(i)
    elif ans[-1] > i:
        ans[bisect_left(ans, i)] = i
print(len(ans))